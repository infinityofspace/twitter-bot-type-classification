import os
import time
from abc import ABC
from datetime import datetime
from enum import Enum
from multiprocessing import Queue, Process, Lock

import requests
import tweepy

from twitter_bot_type_classification.dataset.db import SqliteTweetDB, CsvTweetDB, SqliteUserDB, CsvUserDB
from twitter_bot_type_classification.features.utils import URL_SCHEME

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
NETWORK_CONNECTION_DOWN_ERROR_SUBSTRINGS = ["NewConnectionError",
                                            "Failed to establish a new connection: [Errno -2] Name or service not known"]
ENCODING = "UTF-8"


class FetchWorker(Process):

    def __init__(self, task_q, results_q):
        self.task_q = task_q
        self.results_q = results_q
        super(FetchWorker, self).__init__()

    def run(self):
        while True:
            task = self.task_q.get()
            if task is None:
                self.results_q.put(None)
                break

            task.execute()

            self.results_q.put(task)


class SaveWorker(Process):

    def __init__(self, task_q, db, fetch_worker_count, total_results, std_out_lock):
        self.task_q = task_q
        self.db = db
        self.fetch_worker_count = fetch_worker_count
        self.total_results = total_results
        self.std_out_lock = std_out_lock
        super(SaveWorker, self).__init__()

    def run(self):
        results_saved = 0
        not_available = 0

        while True:
            task = self.task_q.get()
            if task is None:
                self.fetch_worker_count -= 1
                if self.fetch_worker_count == 0:
                    self.std_out_lock.acquire()
                    print("\nAll tasks finished")
                    self.std_out_lock.release()
                    break
            else:
                results = task.get_result()

                if len(results) > 0:
                    self.db.add_many(results)

                results_saved += len(results)

                diff = task.expected_result_length - len(results)
                if diff > 0:
                    not_available += diff
                    # subtract the not available from total count
                    self.total_results -= diff

                self.std_out_lock.acquire()
                print("\rNot available: {} Saved: {}/{}".format(not_available, results_saved, self.total_results),
                      end="", flush=True)
                self.std_out_lock.release()


class FetchTask:
    result = None

    def __init__(self, func, args, expected_result_length):
        self.func = func
        self.args = args
        self.expected_result_length = expected_result_length

    def execute(self):
        self.result = self.func(**self.args)

    def get_result(self):
        return self.result


class DBType(Enum):
    USER = 0
    TWEET = 1


class DatasetGenerator(ABC):
    save_worker = None

    def __init__(self, api, tasks_q_size=100, results_q_size=100):
        assert api is not None
        assert tasks_q_size > 0
        assert results_q_size > 0

        self.api = api
        self.tasks_q_size = tasks_q_size
        self.results_q_size = results_q_size
        self.std_out_lock = Lock()

    def __init_worker__(self, filename, db_type, sqlite, total_length):
        self.tasks_q = Queue(self.tasks_q_size)
        self.results_q = Queue(self.results_q_size)
        self.workers = []

        if sqlite:
            if db_type is DBType.USER:
                db = SqliteUserDB(filename)
            else:
                db = SqliteTweetDB(filename)
        else:
            if db_type is DBType.USER:
                db = CsvUserDB(filename)
            else:
                db = CsvTweetDB(filename)

        for i in range(os.cpu_count()):
            worker = FetchWorker(self.tasks_q, self.results_q)
            self.workers.append(worker)
            worker.start()

        print("{} download worker started.".format(len(self.workers)))

        self.save_worker = SaveWorker(self.results_q, db, len(self.workers), total_length,
                                      self.std_out_lock)
        self.save_worker.start()

    def __stop_worker__(self):
        for _ in range(len(self.workers)):
            self.tasks_q.put(None)


class TweetDatasetGenerator(DatasetGenerator):

    def get_tweets_of_users(self, users, filename=None, limit=200, is_username=False, sqlite=True):
        assert filename is not None
        assert limit > -2 and limit != 0

        self.__init_worker__(filename, DBType.TWEET, sqlite, limit * len(users))

        for u in users:
            self.tasks_q.put(
                FetchTask(self.fetch_tweets_for_user, {"api": self.api, "user": u, "is_username": is_username,
                                                       "limit": limit},
                          limit))

        self.__stop_worker__()

        self.save_worker.join()

    @staticmethod
    def fetch_tweets_for_user(api, user=None, limit=200, is_username=False, tweet_mode="extended"):
        assert api is not None
        assert user is not None
        assert limit is not None

        tweets = []

        if limit > 200:
            count = 200
        else:
            count = limit

        since_id = None
        retries = 5
        network_down_retries = 20

        while True:
            try:
                if is_username:
                    for status in tweepy.Cursor(api.user_timeline, screen_name=user, count=count, since_id=since_id,
                                                trim_user=True, tweet_mode=tweet_mode).items(limit):
                        tweets.append(status)
                else:
                    for status in tweepy.Cursor(api.user_timeline, user_id=user, count=count, since_id=since_id,
                                                trim_user=True, tweet_mode=tweet_mode).items(limit):
                        tweets.append(status)
                break
            except tweepy.error.TweepError as error:
                status_code = getattr(error.response, "status_code", None)
                if status_code == 401:
                    # the Twitter user does not exists anymore
                    break
                elif all(error_substring in error.reason for error_substring in
                         NETWORK_CONNECTION_DOWN_ERROR_SUBSTRINGS):
                    if network_down_retries > 0:
                        __handle_connection_down_error__(network_down_retries)
                        network_down_retries -= 1
                        if len(tweets) > 0:
                            since_id = tweets[-1].id
                        limit = limit - len(tweets)
                        continue
                    else:
                        print(
                            "Network connection is down and max number of retries reached. Stopping current request loop.")
                        break
                else:
                    if retries > 0:
                        print("Error while loading tweets from {} with error response {}".format(user,
                                                                                                 getattr(error,
                                                                                                         "response",
                                                                                                         "unkown")))
                        print("Retry: {}".format(retries))
                        retries -= 1
                        if len(tweets) > 0:
                            since_id = tweets[-1].id
                        limit = limit - len(tweets)
                    else:
                        print("Max number of retries reached. Stopping current request loop.")
                        break

        return [parse_tweet(t) for t in tweets]


class UserDatasetGenerator(DatasetGenerator):

    def get_users(self, users, filename=None, is_username=False, sqlite=True):
        assert filename is not None

        self.__init_worker__(filename, DBType.USER, sqlite, len(users))

        idx = 0
        while idx < len(users):
            temp = users[idx:idx + 100]
            self.tasks_q.put(
                FetchTask(self.fetch_users, {"api": self.api, "users_to_fetch": temp, "is_username": is_username},
                          len(temp)))
            idx += 100

        self.__stop_worker__()

        self.save_worker.join()

    @staticmethod
    def fetch_users(api, users_to_fetch=None, is_username=True, network_down_retries=20):
        assert api is not None
        assert users_to_fetch is not None

        users = []

        if users_to_fetch is not None:
            idx = 0
            while idx < len(users_to_fetch):
                try:
                    if is_username:
                        users.extend(api.lookup_users(screen_names=users_to_fetch[idx:idx + 100]))
                    else:
                        users.extend(api.lookup_users(user_ids=users_to_fetch[idx:idx + 100]))

                except tweepy.error.TweepError as error:
                    status_code = getattr(error.response, "status_code", None)
                    print(error)
                    if status_code == 401 or error.api_code == 17:
                        # the Twitter user(s) does not exists anymore
                        pass
                    elif all(error_substring in error.reason for error_substring in
                             NETWORK_CONNECTION_DOWN_ERROR_SUBSTRINGS):
                        if network_down_retries > 0:
                            __handle_connection_down_error__(network_down_retries)
                            network_down_retries -= 1
                            continue
                        else:
                            print("Network connection is down and max retries reached. Stopping current request loop.")
                            break
                    else:
                        raise error

                idx += 100
        return [parse_user(u) for u in users]


def __handle_connection_down_error__(retries):
    wait_time = int(round(120 / retries) * 5)
    print("The network connection is down. Wait {}s to create new request. {}/20 retires remaining".format(
        wait_time, retries))
    time.sleep(wait_time)


def parse_user(user):
    withheld_in_countries = getattr(user, "withheld_in_countries", None)
    if withheld_in_countries is not None:
        withheld_in_countries = ";".join(withheld_in_countries)

    if user.url is None:
        expanded_url = ""
    else:
        expanded_url = requests.head(user.url).headers["location"]

        if URL_SCHEME.sub("", expanded_url) == URL_SCHEME.sub("", user.url):
            try:
                expanded_url = requests.get(user.url, timeout=10).url
            except requests.exceptions.ConnectionError as e:
                expanded_url = e.request.url
            except requests.exceptions.ReadTimeout as e:
                expanded_url = e.request.url
            except requests.exceptions.TooManyRedirects as e:
                expanded_url = e.request.url

    return [
        user.id,
        user.name.encode("unicode_escape").decode(ENCODING),
        user.screen_name.encode("unicode_escape").decode(ENCODING),
        user.location.encode("unicode_escape").decode(ENCODING),
        user.url,
        expanded_url,
        user.description.encode("unicode_escape").decode(ENCODING),
        user.protected,
        user.verified,
        user.followers_count,
        user.friends_count,
        user.listed_count,
        user.favourites_count,
        user.statuses_count,
        user.created_at,
        user.profile_image_url_https,
        user.default_profile,
        user.default_profile_image,
        withheld_in_countries,
        datetime.now().strftime(DATETIME_FORMAT)
    ]


def parse_tweet(tweet):
    withheld_in_countries = getattr(tweet, "withheld_in_countries", None)
    withheld_in_countries_str = None
    if withheld_in_countries is not None:
        withheld_in_countries_str = ";".join(withheld_in_countries)

    retweeted_status = getattr(tweet, "retweeted_status", None)
    if retweeted_status is not None:
        text = retweeted_status.full_text
        retweeted_status_id = retweeted_status.id
    else:
        text = tweet.full_text
        retweeted_status_id = None
    if text is not None:
        text = text.encode("unicode_escape").decode(ENCODING)

    coordinates = getattr(tweet, "coordinates", None)
    coordinates_str = None
    if coordinates is not None:
        coordinates_str = ";".join(map(str, coordinates["coordinates"]))

    quoted_status = getattr(tweet, "quoted_status", None)
    quoted_status_text = None
    if quoted_status is not None:
        quoted_status_text = quoted_status.full_text
    if quoted_status_text is not None:
        quoted_status_text = quoted_status_text.encode("unicode_escape").decode(ENCODING)

    urls = {}
    for url in tweet.entities["urls"]:
        urls[url["url"]] = url["expanded_url"]

    videos = 0
    photos = 0
    gifs = 0

    if hasattr(tweet, "extended_entities"):
        for media in tweet.extended_entities.get("media", []):
            if media["type"] == "photo":
                photos += 1
            elif media["type"] == "video":
                videos += 1
            elif media["type"] == "animated_gif":
                gifs += 1

    return [
        tweet.id,
        tweet.user.id,
        tweet.created_at,
        text,
        coordinates_str,
        tweet.place.country_code if tweet.place is not None else None,
        tweet.place.name if tweet.place is not None else None,
        tweet.in_reply_to_status_id,
        tweet.in_reply_to_user_id,
        getattr(tweet, "quoted_status_id", None),
        quoted_status_text,
        retweeted_status_id,
        tweet.retweet_count,
        tweet.favorite_count,
        getattr(tweet, "lang", None),
        getattr(tweet, "withheld_copyright", False),
        withheld_in_countries_str,
        str(urls),
        videos,
        photos,
        gifs,
        tweet.source,
        datetime.now().strftime(DATETIME_FORMAT)
    ]
