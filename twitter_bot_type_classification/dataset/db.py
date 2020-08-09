import ast
import csv
import linecache
import sqlite3
from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime
from io import StringIO

from tweepy import Status, User

USER_HEADER = [
    "id",
    "name",
    "screen_name",
    "location",
    "url",
    "expanded_url",
    "description",
    "protected",
    "verified",
    "followers_count",
    "friends_count",
    "listed_count",
    "favourites_count",
    "statuses_count",
    "created_at",
    "profile_image_url_https",
    "default_profile",
    "default_profile_image",
    "withheld_in_countries",
    "fetch_date"
]

TWEET_HEADER = [
    "id",
    "user_id",
    "created_at",
    "text",
    "coordinates",
    "country_code",
    "place_name",
    "in_reply_to_status_id",
    "in_reply_to_user_id",
    "quoted_status_id",
    "quoted_status_text",
    "retweeted_status_id",
    "retweet_count",
    "favorite_count",
    "lang",
    "withheld_copyright",
    "withheld_in_countries",
    "urls",
    "videos",
    "photos",
    "gifs",
    "source",
    "fetch_date"
]

TWITTER_DATE_TIME_FORMAT = "%a %b %d %H:%M:%S %Y"

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class UserDB(ABC):

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def add_many(self, items):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass

    @abstractmethod
    def get_all_user(self):
        pass

    @staticmethod
    def parse_user(row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";"):
        user_dic = {
            "id": int(row[0]),
            "name": row[1].encode(file_encoding).decode(text_encoding),
            "screen_name": row[2],
            "location": row[3],
            "url": None if row[4] == "" or row[4] is None else row[4],
            "description": row[6].encode(file_encoding).decode(text_encoding),
            "protected": True if row[7] == "True" else False,
            "verified": True if row[8] == "True" else False,
            "followers_count": int(row[9]),
            "friends_count": int(row[10]),
            "listed_count": int(row[11]),
            "favourites_count": int(row[12]),
            "statuses_count": int(row[13]),
            "created_at": datetime.strptime(row[14], DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": row[15],
            "default_profile": True if row[16] == "True" else False,
            "default_profile_image": True if row[17] == "True" else False,
            "withheld_in_countries": None if row[18] == "" or row[18] is None else row[18].split(list_separator),
            # the following attributes are only present in dataset, the normal tweepy Status object does not
            # contain these attributes
            "expanded_url": None if row[5] == "" else row[5],
            "fetch_date": datetime.strptime(row[19], DATE_TIME_FORMAT)
        }

        return User.parse(api=None, json=user_dic)


class TweetDB(ABC):

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def add_many(self, items):
        pass

    @abstractmethod
    def get_tweets_for_user(self, user_id):
        pass

    @abstractmethod
    def get_tweets_grouped_by_user(self):
        pass

    @staticmethod
    def parse_tweet(row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";"):
        urls_dict = ast.literal_eval(row[17])
        urls = []
        for url, expanded_url in urls_dict.items():
            urls.append({"url": url, "expanded_url": expanded_url})

        coordinates = None
        if row[4] != "" and row[4] is not None:
            coords = row[4].split(";")
            if len(coords) > 1:
                coordinates = {
                    "coordinates": [float(coords[0]), float(coords[1])]
                }

        tweet_dic = {
            "id": int(row[0]),
            "user_id": int(row[1]),
            "created_at": datetime.strptime(row[2], DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": row[3].encode(file_encoding).decode(text_encoding),
            "coordinates": coordinates,
            "place": None if row[5] == "" or row[5] is None else {
                "country_code": row[5],
                "name": row[6]
            },
            "in_reply_to_status_id": None if row[7] == "" or row[7] is None else int(row[7]),
            "in_reply_to_user_id": None if row[8] == "" or row[8] is None else int(row[8]),
            "quoted_status_id": None if row[9] == "" or row[9] is None else int(row[9]),
            "retweet_count": int(row[12]),
            "favorite_count": int(row[13]),
            "lang": row[14],
            "withheld_copyright": True if row[15] == "True" else False,
            "withheld_in_countries": None if row[16] == "" or row[16] is None else row[16].split(list_separator),
            "entities": {
                "urls": urls
            },
            "source": row[21],
            # the following attributes are only present in dataset, the normal tweepy Status object does not
            # contains these attributes
            "videos": int(row[18]),  # the number of videos included in the tweet
            "photos": int(row[19]),  # the number of photos included in the tweet
            "gifs": int(row[20]),  # the number of gifs included in the tweet
            "fetch_date": datetime.strptime(row[22], DATE_TIME_FORMAT),
            # the date when the tweet was fetched
        }

        if row[10] != "" and row[10] is not None:
            tweet_dic["quoted_status"] = {
                "text": row[10].encode(file_encoding).decode(text_encoding)
            }

        if row[11] != "" and row[11] is not None:
            tweet_dic["retweeted_status"] = {
                "id": int(row[11])
            }

        return Status.parse(api=None, json=tweet_dic)


class SqliteTweetDB(TweetDB):

    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)

        c = self.conn.cursor()

        if not c.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'tweet'").fetchone():
            print("New sqlite tweets db created")
            c.execute("""CREATE TABLE tweet (
                            "id" INTEGER PRIMARY KEY,
                            "user_id" INTEGER,
                            "created_at" TEXT,
                            "text" TEXT,
                            "coordinates" TEXT,
                            "country_code" TEXT,
                            "place_name" TEXT,
                            "in_reply_to_status_id" INTEGER,
                            "in_reply_to_user_id" INTEGER,
                            "quoted_status_id" INTEGER,
                            "quoted_status_text" TEXT,
                            "retweeted_status_id" INTEGER,
                            "retweet_count" INTEGER,
                            "favorite_count" INTEGER,
                            "lang" TEXT,
                            "withheld_copyright" INTEGER,
                            "withheld_in_countries" TEXT,
                            "urls" INTEGER,
                            "videos" INTEGER,
                            "photos" INTEGER,
                            "gifs" INTEGER,
                            "source" TEXT,
                            "fetch_date" TEXT
                        )
                    """)

    def get_tweets_grouped_by_user(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM tweet WHERE user_id IN (SELECT user_id FROM tweet GROUP BY user_id)")
        return c

    def get_tweets_for_user(self, user_id):
        c = self.conn.cursor()
        c.execute("SELECT * FROM tweet WHERE user_id == ? ORDER BY id DESC", (user_id,))
        return [self.parse_tweet(t) for t in list(c)]

    def add(self, tweet):
        c = self.conn.cursor()
        c.execute("INSERT INTO tweet VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  tweet)
        self.conn.commit()

    def add_many(self, tweets):
        c = self.conn.cursor()
        c.executemany("INSERT INTO tweet VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      tweets)
        self.conn.commit()


class SqliteUserDB(UserDB):

    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)

        c = self.conn.cursor()
        if not c.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'user'").fetchone():
            print("New sqlite users db created")
            c.execute("""CREATE TABLE user (
                            "id" INTEGER PRIMARY KEY,
                            "name" TEXT,
                            "screen_name" TEXT,
                            "location" TEXT,
                            "url" TEXT,
                            "expanded_url" TEXT,
                            "description" TEXT,
                            "protected" INTEGER,
                            "verified" INTEGER,
                            "followers_count" INTEGER,
                            "friends_count" INTEGER,
                            "listed_count" INTEGER,
                            "favourites_count" INTEGER,
                            "statuses_count" INTEGER,
                            "created_at" TEXT,
                            "profile_image_url_https" TEXT,
                            "default_profile" INTEGER,
                            "default_profile_image" INTEGER,
                            "withheld_in_countries" TEXT,
                            "fetch_date" TEXT
                          )
                        """)
            self.conn.commit()

    def get_user(self, user_id):
        c = self.conn.cursor()
        return c.execute("SELECT * FROM user WHERE id = ?", user_id).fetchone()[0]

    def get_total_number_of_users(self):
        c = self.conn.cursor()
        return c.execute("SELECT count(*) FROM user").fetchone()[0]

    def get_all_user(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM user")

        return [self.parse_user(u) for u in c.fetchall()]

    def add(self, user):
        c = self.conn.cursor()
        c.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", user)
        self.conn.commit()

    def add_many(self, users):
        c = self.conn.cursor()
        c.executemany("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", users)
        self.conn.commit()


class CsvDB:

    def __init__(self, filename, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL, encoding="UTF-8",
                 skip_header=False):
        self.filename = filename
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.quoting = quoting
        self.encoding = encoding
        self.skip_header = skip_header

    def add(self, user):
        with open(self.filename, "a", encoding=self.encoding) as f:
            writer = csv.writer(f, delimiter=self.delimiter, quotechar=self.quotechar, quoting=self.quoting)
            if f.tell() == 0:
                self.__write_header__(writer)

            writer.writerow(user)

    def add_many(self, users):
        with open(self.filename, "a", encoding=self.encoding) as f:
            writer = csv.writer(f, delimiter=self.delimiter, quotechar=self.quotechar, quoting=self.quoting)
            if f.tell() == 0:
                self.__write_header__(writer)

            writer.writerows(users)

    @abstractmethod
    def __write_header__(self, writer):
        pass


class CsvTweetDB(CsvDB, TweetDB):

    def __init__(self, filename, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL, encoding="UTF-8",
                 skip_header=False,
                 fast_read=False):
        super().__init__(filename, delimiter, quotechar, quoting, encoding, skip_header)

        self.fast_read = fast_read

        # create a previously calculated index for reading big csv file
        if fast_read:
            self.tweet_user_id_index = defaultdict(list)

            with open(self.filename, "r", encoding=self.encoding) as f:
                reader = csv.reader(f, delimiter=self.delimiter, quotechar=self.quotechar,
                                    quoting=self.quoting)

                if self.skip_header:
                    next(reader)

                for i, r in enumerate(reader):
                    self.tweet_user_id_index[r[1]].append(i)

    def __write_header__(self, writer):
        writer.writerow(TWEET_HEADER)

    def get_tweets_for_user(self, user_id):
        tweets = []

        if self.fast_read:
            tweets_idx = self.tweet_user_id_index.get(user_id, None)
            if tweets_idx is not None:
                string_tweets = []
                for i in tweets_idx:
                    string_tweets.append(linecache.getline(self.filename, i))

                for t in string_tweets:
                    reader = csv.reader(StringIO(t), delimiter=self.delimiter, quotechar=self.quotechar,
                                        quoting=self.quoting)
                    tweets.append(self.parse_tweet(next(reader)))

            else:
                print("Warning: no tweets for user if found")

            return tweets
        else:
            with open(self.filename, "r", encoding=self.encoding) as f:
                reader = csv.reader(f, delimiter=self.delimiter, quotechar=self.quotechar,
                                    quoting=self.quoting)

                if self.skip_header:
                    next(reader)

                for r in reader:
                    if r[1] == str(user_id):
                        tweets.append(self.parse_tweet(r))

        return tweets

    def get_tweets_grouped_by_user(self):
        # TODO: add option to get tweets without user id (helpful when there is no user db)
        raise NotImplementedError


class CsvUserDB(CsvDB, UserDB):

    def __init__(self, filename, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL, encoding="UTF-8",
                 skip_header=False):
        super().__init__(filename, delimiter, quotechar, quoting, encoding, skip_header)

    def __write_header__(self, writer):
        writer.writerow(USER_HEADER)

    def get_user(self, user_id):
        users = []
        with open(self.filename, "r", encoding=self.encoding) as f:
            reader = csv.reader(f, delimiter=self.delimiter, quotechar=self.quotechar,
                                quoting=self.quoting)

            if self.skip_header:
                next(reader)

            for r in reader:
                if r[0] == str(user_id):
                    users.append(self.parse_user(r))

        return users

    def get_all_user(self):
        users = []
        with open(self.filename, "r", encoding=self.encoding) as f:
            reader = csv.reader(f, delimiter=self.delimiter, quotechar=self.quotechar,
                                quoting=self.quoting)

            if self.skip_header:
                next(reader)

            for r in reader:
                users.append(self.parse_user(r))

        return users
