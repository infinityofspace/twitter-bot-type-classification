import unittest
from datetime import datetime

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tweepy import Status, User

from twitter_bot_type_classification.dataset.db import DATE_TIME_FORMAT, TWITTER_DATE_TIME_FORMAT
from twitter_bot_type_classification.features.tweet import TweetFeatures, TWEET_SOURCES_IDX, COUNTRY_CODES_IDX, \
    TWEET_TEXT_SIMILARITY_FEATURES
from twitter_bot_type_classification.features.user import UserFeatures, USER_FEATURES_INDEX


class UserFeaturesTests(unittest.TestCase):

    def test_tweet_time_interval_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_time_interval_mean"]]))

    def test_tweet_time_interval_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:05:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:10:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 3,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:50:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 4,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 01:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 5,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 01:05:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweet_time_interval_mean"]], np.mean([
            946681200.0 - 946681500.0, 946681500.0 - 946681800.0, 946681800.0 - 946684200.0, 946684200.0 - 946684800.0,
            946684800.0 - 946685100.0
        ]), places=4)

    def test_tweet_time_interval_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_time_interval_std"]]))

    def test_tweet_time_interval_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:05:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:10:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 3,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:50:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 4,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 01:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 5,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 01:05:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweet_time_interval_std"]], np.std([
            946681200.0 - 946681500.0, 946681500.0 - 946681800.0, 946681800.0 - 946684200.0, 946684200.0 - 946684800.0,
            946684800.0 - 946685100.0
        ]), places=4)

    def test_tweet_likes_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_likes_mean"]]))

    def test_tweet_likes_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 10,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 5,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["tweet_likes_mean"]], np.mean([10, 3, 5]))

    def test_tweet_likes_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_likes_std"]]))

    def test_tweet_likes_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 10,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 5,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweet_likes_std"]], np.std([10, 3, 5]), places=6)

    def test_tweet_likes_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_likes_max"]]))

    def test_tweet_likes_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 10,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 5,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["tweet_likes_max"]], 10)

    def test_tweet_likes_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_likes_min"]]))

    def test_tweet_likes_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 10,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 5,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["tweet_likes_min"]], 3)

    def test_tweet_retweets_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_retweets_mean"]]))

    def test_tweet_retweets_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 1,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 3,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 7,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweet_retweets_mean"]], np.mean([1, 3, 7]), places=6)

    def test_tweet_retweets_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_retweets_std"]]))

    def test_tweet_retweets_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 1,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 3,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 7,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweet_retweets_std"]], np.std([1, 3, 7]), places=6)

    def test_tweet_retweets_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_retweets_max"]]))

    def test_tweet_retweets_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 1,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 3,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 7,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["tweet_retweets_max"]], 7)

    def test_tweet_retweets_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_retweets_min"]]))

    def test_tweet_retweets_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 1,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 3,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 7,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["tweet_retweets_min"]], 1.0)

    def test_self_replies_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["self_replies_mean"]]))

    def test_self_replies_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": 5,
                "in_reply_to_user_id": 1,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": 5,
                "in_reply_to_user_id": 1,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["self_replies_mean"]], np.mean([1, 1, 0]))

    def test_number_of_different_countries_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_different_countries"]]))

    def test_number_of_different_countries(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": {
                    "country_code": "DE",
                    "name": "Berlin"
                },
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": {
                    "country_code": "DE",
                    "name": "Berlin"
                },
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": {
                    "country_code": "EN",
                    "name": "London"
                },
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_different_countries"]], 2.0)

    def test_country_with_most_tweets_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["country_with_most_tweets"]]))

    def test_country_with_most_tweets(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": {
                    "country_code": "DE",
                    "name": "Berlin"
                },
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": {
                    "country_code": "DE",
                    "name": "Berlin"
                },
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": {
                    "country_code": "EN",
                    "name": "London"
                },
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["country_with_most_tweets"]], COUNTRY_CODES_IDX["DE"])

    def test_number_of_different_sources_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_different_sources"]]))

    def test_number_of_different_sources(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Android App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_different_sources"]], 2.0)

    def test_most_used_source_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["most_used_source"]]))

    def test_most_used_source(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Android App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["most_used_source"]], TWEET_SOURCES_IDX["Twitter Web App"])

    def test_retweet_tweets_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["retweet_tweets_mean"]]))

    def test_retweet_tweets_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 12
                }
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 13
                }
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["retweet_tweets_mean"]], np.mean([1, 1, 0]))

    def test_answer_tweets_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["answer_tweets_mean"]]))

    def test_answer_tweets_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": 12,
                "in_reply_to_user_id": 42,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": 13,
                "in_reply_to_user_id": 42,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["answer_tweets_mean"]], np.mean([1, 1, 0]))

    def test_number_of_withheld_countries_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_withheld_countries_max"]]))

    def test_number_of_withheld_countries_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": ["EN"],
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": ["DE", "EN", "NL"],
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_withheld_countries_max"]], 3.0)

    def test_withheld_country_tweets_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["withheld_country_tweets_mean"]]))

    def test_withheld_country_tweets_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": "DE",
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["withheld_country_tweets_mean"]], np.mean([0, 0, 1]))

    def test_number_of_different_tweet_coord_groups_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_different_tweet_coord_groups"]]))

    def test_number_of_different_tweet_coord_groups_group(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": {
                    "coordinates": [15, -74]
                },
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": {
                    "coordinates": [0, -74]
                },
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_different_tweet_coord_groups"]], 2)

    def test_most_frequent_tweet_coord_group_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["most_frequent_tweet_coord_group"]]))

    def test_most_frequent_tweet_coord_group(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": {
                    "coordinates": [15, -74]
                },
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": {
                    "coordinates": [0, -74]
                },
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["most_frequent_tweet_coord_group"]], 7.0)

    def test_different_user_interactions_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["different_user_interactions"]]))

    def test_different_user_interactions_0(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["different_user_interactions"]], 0)

    def test_different_user_interactions_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 12345,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["different_user_interactions"]], 1)

    def test_different_user_interactions_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 12345,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 12345,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["different_user_interactions"]], 1)

    def test_different_user_interactions_3(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 12345,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 12345,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 56789,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["different_user_interactions"]], 2)

    def test_different_user_interactions_4(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 12345,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 56789,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": 101112,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["different_user_interactions"]], 3)

    def test_tweet_text_length_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_text_length_max"]]))

    def test_tweet_text_length_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["tweet_text_length_max"]], 108)

    def test_tweet_text_length_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_text_length_min"]]))

    def test_tweet_text_length_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["tweet_text_length_min"]], 53)

    def test_tweet_text_length_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_text_length_mean"]]))

    def test_tweet_text_length_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweet_text_length_mean"]], np.mean([61, 108, 53]),
                               places=5)

    def test_tweet_text_length_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweet_text_length_std"]]))

    def test_tweet_text_length_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweet_text_length_std"]], np.std([61, 108, 53]),
                               places=5)

    def test_number_of_hashtags_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_hashtags_max"]]))

    def test_number_of_hashtags_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #ab #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_hashtags_max"]], 2.0)

    def test_number_of_hashtags_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_hashtags_min"]]))

    def test_number_of_hashtags_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #ab #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_hashtags_min"]], 0.0)

    def test_number_of_hashtags_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_hashtags_mean"]]))

    def test_number_of_hashtags_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #ab #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_hashtags_mean"]], np.mean([0, 2, 1]))

    def test_number_of_hashtags_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_hashtags_std"]]))

    def test_number_of_hashtags_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #ab #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_hashtags_std"]], np.std([0, 2, 1]))

    def test_length_of_hashtag_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["length_of_hashtag_max"]]))

    def test_length_of_hashtag_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #ab #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["length_of_hashtag_max"]], 6.0)

    def test_length_of_hashtag_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["length_of_hashtag_min"]]))

    def test_length_of_hashtag_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #ab #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["length_of_hashtag_min"]], 3.0)

    def test_cleaned_tweet_text_length_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_max"]]))

    def test_cleaned_tweet_text_length_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_max"]], 63.0)

    def test_cleaned_tweet_text_length_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_min"]]))

    def test_cleaned_tweet_text_length_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_min"]], 39.0)

    def test_cleaned_tweet_text_length_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_mean"]]))

    def test_cleaned_tweet_text_length_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_mean"]],
                               np.mean([39, 63, 51]))

    def test_cleaned_tweet_text_length_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_std"]]))

    def test_cleaned_tweet_text_length_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": " 😀 This is just a simple test tweet text with urls and emojis. http://www.twitter.com http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text with emojis. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["cleaned_tweet_text_length_std"]],
                               np.std([39, 63, 51]), places=6)

    def test_number_of_user_mentions_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_user_mentions_mean"]]))

    def test_number_of_user_mentions_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2 @user3",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_user_mentions_mean"]], np.mean([3, 2, 1]))

    def test_number_of_user_mentions_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_user_mentions_std"]]))

    def test_number_of_user_mentions_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2 @user3",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_user_mentions_std"]], np.std([3, 2, 1]))

    def test_number_of_user_mentions_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_user_mentions_max"]]))

    def test_number_of_user_mentions_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2 @user3",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_user_mentions_max"]], 3.0)

    def test_number_of_user_mentions_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_user_mentions_min"]]))

    def test_number_of_user_mentions_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2 @user3",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user1 @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. @user2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_user_mentions_min"]], 1.0)

    def test_number_of_sentences_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_sentences_mean"]]))

    def test_number_of_sentences_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. This is another sentence.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_sentences_mean"]], np.mean([1, 1, 2]))

    def test_number_of_sentences_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_sentences_std"]]))

    def test_number_of_sentences_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. This is another sentence.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_sentences_std"]], np.std([1, 1, 2]))

    def test_number_of_words_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_words_mean"]]))

    def test_number_of_words_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text and some more words than before.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_words_mean"]], np.mean([8, 8, 14]))

    def test_number_of_words_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_words_std"]]))

    def test_number_of_words_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text and some more words than before.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_words_std"]], np.std([8, 8, 14]))

    def test_number_of_emojis_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_emojis_mean"]]))

    def test_number_of_emojis_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.😀😀😀😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. 😀😀😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_mean"]], np.mean([5, 2, 4]),
                               places=6)

    def test_number_of_emojis_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_emojis_std"]]))

    def test_number_of_emojis_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.😀😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.😀😀😀😀😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_std"]], np.std([3, 2, 6]))

    def test_number_of_emojis_max_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_emojis_max"]]))

    def test_number_of_emojis_max(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. 😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. 😀😀😀 😀 😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_max"]], 5.0)

    def test_number_of_emojis_min_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_emojis_min"]]))

    def test_number_of_emojis_min(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. 😀 😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.😀😀😀😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_min"]], 1.0)

    def test_emoji_only_tweets_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["emoji_only_tweets_mean"]]))

    def test_emoji_only_tweets_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "😀 😀😀 😀😀 😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "😀 😀",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["emoji_only_tweets_mean"]], np.mean([0, 1, 1]))

    def test_number_of_tweet_languages_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_tweet_languages"]]))

    def test_number_of_tweet_languages(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "Dies ist ein Testext.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "de",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_tweet_languages"]], 2)

    def test_most_used_tweet_language_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["most_used_tweet_language"]]))

    def test_most_used_tweet_language(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "Dies ist ein Testext.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "de",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertEqual(user_features[USER_FEATURES_INDEX["most_used_tweet_language"]], 41.0)

    def test_pagination_tweets_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["pagination_tweets_mean"]]))

    def test_pagination_tweets_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "2/2 This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. (2/2)",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["pagination_tweets_mean"]], np.mean([0, 1, 1]))

    def test_own_tweets_text_similarity_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["own_tweets_text_similarity_mean"]]))

    def test_own_tweets_text_similarity_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        tweet_features_1 = TweetFeatures(tweets[0], user)[TWEET_TEXT_SIMILARITY_FEATURES]
        tweet_features_2 = TweetFeatures(tweets[1], user)[TWEET_TEXT_SIMILARITY_FEATURES]
        tweet_features_3 = TweetFeatures(tweets[2], user)[TWEET_TEXT_SIMILARITY_FEATURES]

        similarity = cosine_similarity([tweet_features_1, tweet_features_2, tweet_features_3])

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["own_tweets_text_similarity_mean"]], similarity.mean())

    def test_own_tweets_text_similarity_mean_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. #test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["own_tweets_text_similarity_mean"]], -1)

    def test_own_tweets_text_similarity_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["own_tweets_text_similarity_std"]]))

    def test_own_tweets_text_similarity_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        tweet_features_1 = TweetFeatures(tweets[0], user)[TWEET_TEXT_SIMILARITY_FEATURES]
        tweet_features_2 = TweetFeatures(tweets[1], user)[TWEET_TEXT_SIMILARITY_FEATURES]
        tweet_features_3 = TweetFeatures(tweets[2], user)[TWEET_TEXT_SIMILARITY_FEATURES]

        similarity = cosine_similarity([tweet_features_1, tweet_features_2, tweet_features_3])

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["own_tweets_text_similarity_std"]], similarity.std())

    def test_own_tweets_text_similarity_std_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            })
        ]

        tweet_features_1 = TweetFeatures(tweets[0], user)[TWEET_TEXT_SIMILARITY_FEATURES]
        tweet_features_2 = TweetFeatures(tweets[1], user)[TWEET_TEXT_SIMILARITY_FEATURES]

        similarity = cosine_similarity([tweet_features_1, tweet_features_2])

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["own_tweets_text_similarity_std"]], similarity.std())

    def test_retweet_tweets_text_similarity_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_mean"]]))

    def test_retweet_tweets_text_similarity_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_mean"]], -1)

    def test_retweet_tweets_text_similarity_mean_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_mean"]], 1)

    def test_retweet_tweets_text_similarity_mean_3(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. Here is some more text and an url https://www.test.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        tweet_features_1 = TweetFeatures(tweets[0], user)[TWEET_TEXT_SIMILARITY_FEATURES]
        tweet_features_2 = TweetFeatures(tweets[1], user)[TWEET_TEXT_SIMILARITY_FEATURES]

        similarity = cosine_similarity([tweet_features_1, tweet_features_2])

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_mean"]],
                               np.mean(similarity))

    def test_retweet_tweets_text_similarity_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_std"]]))

    def test_retweet_tweets_text_similarity_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_std"]], -1)

    def test_retweet_tweets_text_similarity_std_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_std"]], -1)

    def test_retweet_tweets_text_similarity_std_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT),
                "retweeted_status": {
                    "id": 1
                }
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        tweet_features_1 = TweetFeatures(tweets[0], user)[TWEET_TEXT_SIMILARITY_FEATURES]
        tweet_features_2 = TweetFeatures(tweets[1], user)[TWEET_TEXT_SIMILARITY_FEATURES]

        similarity = cosine_similarity([tweet_features_1, tweet_features_2])

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["retweet_tweets_text_similarity_std"]],
                               np.std(similarity))

    def test_number_of_url_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_url_mean"]]))

    def test_number_of_url_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_url_mean"]], np.mean([0, 1, 1]))

    def test_number_of_url_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_url_std"]]))

    def test_number_of_url_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com http://www.twitter.com/test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_url_std"]], np.std([0, 1, 2]))

    def test_total_urls_vs_urls_domain_matches_username_ratio_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(
            np.isnan(user_features[USER_FEATURES_INDEX["total_urls_vs_urls_domain_matches_username_ratio"]]))

    def test_total_urls_vs_urls_domain_matches_username_ratio(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "testaccount",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com http://www.testaccount.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.testaccount.com/abc",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["total_urls_vs_urls_domain_matches_username_ratio"]],
                               (1 + 2 + 1) / 2)

    def test_total_urls_vs_total_profile_url_domain_matches_ratio_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(
            np.isnan(user_features[USER_FEATURES_INDEX["total_urls_vs_total_profile_url_domain_matches_ratio"]]))

    def test_total_urls_vs_total_profile_url_domain_matches_ratio(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test-account.com",
            "expanded_url": "http://www.test-account.com",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.test-account.com/test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.test-account.com/test2",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(
            user_features[USER_FEATURES_INDEX["total_urls_vs_total_profile_url_domain_matches_ratio"]], (1 + 1 + 1) / 2)

    def test_total_urls_vs_total_other_shortened_urls_ratio_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["total_urls_vs_total_other_shortened_urls_ratio"]]))

    def test_total_urls_vs_total_other_shortened_urls_ratio(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com/test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://bit.ly/test",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["total_urls_vs_total_other_shortened_urls_ratio"]],
                               (1 + 1 + 1) / 1)

    def test_tweets_with_only_urls_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["tweets_with_only_urls_mean"]]))

    def test_tweets_with_only_urls_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text. http://www.twitter.com",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweets_with_only_urls_mean"]], np.mean([0, 1, 0]))

    def test_number_of_photos_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_gifs_mean"]]))

    def test_number_of_photos_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 1,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 3,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_photos_mean"]], np.mean([1, 0, 3]))

    def test_number_of_photos_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_photos_std"]]))

    def test_number_of_photos_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 1,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 3,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_photos_std"]], np.std([1, 0, 3]), delta=7)

    def test_number_of_gifs_mean_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_gifs_mean"]]))

    def test_number_of_gifs_mean(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 2,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 1,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_gifs_mean"]], np.mean([0, 2, 1]))

    def test_number_of_gifs_std_nan(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(np.isnan(user_features[USER_FEATURES_INDEX["number_of_gifs_std"]]))

    def test_number_of_gifs_std(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        tweets = [
            Status.parse(api=None, json={
                "id": 0,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 0,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 1,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 2,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            }),
            Status.parse(api=None, json={
                "id": 2,
                "user_id": 1,
                "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(
                    TWITTER_DATE_TIME_FORMAT),
                "text": "This is just a simple test tweet text.",
                "coordinates": None,
                "place": None,
                "in_reply_to_status_id": None,
                "in_reply_to_user_id": None,
                "quoted_status_id": None,
                "retweet_count": 2,
                "favorite_count": 3,
                "lang": "en",
                "withheld_copyright": False,
                "withheld_in_countries": None,
                "entities": {
                    "urls": []
                },
                "source": "Twitter Web App",
                "videos": 0,
                "photos": 0,
                "gifs": 1,
                "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
            })
        ]

        user_features = UserFeatures(user, tweets)

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["number_of_gifs_std"]], np.std([0, 2, 1]))

    def test_number_of_user_mentions_in_description_empty(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_user_mentions_in_description"]], 0.0)

    def test_number_of_user_mentions_in_description_not_empty_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_user_mentions_in_description"]], 0.0)

    def test_number_of_user_mentions_in_description_not_empty_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text. @user1 @user2",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_user_mentions_in_description"]], 2.0)

    def test_number_description_urls_empty(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_description_urls"]], 0.0)

    def test_number_description_urls_not_empty_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_description_urls"]], 0.0)

    def test_number_description_urls_not_empty_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text with two urls http://www.twitter.com http://www.test.com/test1",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_description_urls"]], 2.0)

    def test_description_url_contains_username_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["description_url_contains_username"]])

    def test_description_url_contains_username_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["description_url_contains_username"]])

    def test_description_url_contains_username_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text with a link http://www.test-account.com",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["description_url_contains_username"]])

    def test_description_url_contains_name_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["description_url_contains_name"]])

    def test_description_url_contains_name_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["description_url_contains_name"]])

    def test_description_link_contains_name_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text with a link http://www.test-account.com",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["description_url_contains_name"]])

    def test_description_length_empty(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["description_length"]], 0.0)

    def test_description_length_not_empty(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a test description with an 😀.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["description_length"]],
                         len("This is a test description with an 😀."))

    def test_number_of_numbers_in_description_0(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_numbers_in_description"]], 0.0)

    def test_number_of_numbers_in_description_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_numbers_in_description"]], 0.0)

    def test_number_of_numbers_in_description_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text with 2 numbers, 1.5 and 2,8 other test values.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_numbers_in_description"]], 3.0)

    def test_number_of_emojis_in_description_0(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_in_description"]], 0.0)

    def test_number_of_emojis_in_description_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_in_description"]], 0.0)

    def test_number_of_emojis_in_description_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text with 😀 😀.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_in_description"]], 2.0)

    def test_number_of_emojis_in_description_3(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text with 😀 😀.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_in_description"]], 2.0)

    def test_description_contains_bot_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["description_contains_bot"]])

    def test_description_contains_bot_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["description_contains_bot"]])

    def test_description_contains_bot_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "This is a sample text and I am a bot.",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["description_contains_bot"]])

    def test_username_length(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_length"]], len("test_account"))

    def test_username_contains_name_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Name",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["username_contains_name"]])

    def test_username_contains_name_True_1(self):
        user_dic = {
            "id": 1,
            "name": "TestAccount",
            "screen_name": "testaccount",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["username_contains_name"]])

    def test_username_contains_name_True_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["username_contains_name"]])

    def test_number_of_char_numbers_in_username_0(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_char_numbers_in_username"]], 0.0)

    def test_number_of_char_numbers_in_username_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account12",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_char_numbers_in_username"]], 2.0)

    def test_username_structure_0(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "username",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 0)

    def test_username_structure_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "USERNAME",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 1)

    def test_username_structure_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "Username",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 2)

    def test_username_structure_3(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "123456",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 3)

    def test_username_structure_4(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "username123",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 4)

    def test_username_structure_5(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "USERNAME123",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 5)

    def test_username_structure_6(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "Username123",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 6)

    def test_username_structure_7(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "1234username",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 7)

    def test_username_structure_8(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "123USERNAME",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 8)

    def test_username_structure_9(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "123Username",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 9)

    def test_username_structure_10(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "123Test123",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 10)

    def test_username_structure_11(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test123Test",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 11)

    def test_username_structure_12(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "__username123__",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 12)

    def test_username_structure_13(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], 13)

    def test_username_structure_14(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "__test_123",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["username_structure"]], -1)

    def test_username_contains_bot_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["username_contains_bot"]])

    def test_username_contains_bot_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account_bot",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["username_contains_bot"]])

    def test_name_length(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["name_length"]], len("Test Account"))

    def test_number_of_numbers_in_name_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_numbers_in_name"]], 0.0)

    def test_number_of_numbers_in_name_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account 151",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_numbers_in_name"]], 3.0)

    def test_number_of_emojis_in_name_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_in_name"]], 0.0)

    def test_number_of_emojis_in_name_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account 😀 😀",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_emojis_in_name"]], 2.0)

    def test_name_contains_bot_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["name_contains_bot"]])

    def test_name_contains_bot_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account bot",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["name_contains_bot"]])

    def test_profile_url_to_other_service_profile_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_to_other_service_profile"]])

    def test_profile_url_to_other_service_profile_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com",
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_to_other_service_profile"]])

    def test_profile_url_to_other_service_profile_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.facebook.com/test_account_2",
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_to_other_service_profile"]])

    def test_profile_url_domain_contains_username_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_username"]])

    def test_profile_url_domain_contains_username_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com",
            "expanded_url": "http://www.test.com",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_username"]])

    def test_profile_url_domain_contains_username_False_3(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com/test_account",
            "expanded_url": "http://www.test.com/test_account",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_username"]])

    def test_profile_url_domain_contains_username_True_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test_account.com/",
            "expanded_url": "http://www.test_account.com/",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_username"]])

    def test_profile_url_domain_contains_username_True_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.testaccount.com/",
            "expanded_url": "http://www.testaccount.com/",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_username"]])

    def test_profile_url_domain_contains_name_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_name"]])

    def test_profile_url_domain_contains_name_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com",
            "expanded_url": "http://www.test.com",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_name"]])

    def test_profile_url_domain_contains_name_False_3(self):
        user_dic = {
            "id": 1,
            "name": "TestAccountName",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com/TestAccountName",
            "expanded_url": "http://www.test.com/TestAccountName",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_name"]])

    def test_profile_url_domain_contains_name_True_1(self):
        user_dic = {
            "id": 1,
            "name": "TestAccountName",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.testaccountname.com/",
            "expanded_url": "http://www.testaccountname.com/",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_name"]])

    def test_profile_url_domain_contains_name_True_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account Name",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.testaccountname.com/",
            "expanded_url": "http://www.testaccountname.com/",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_domain_contains_name"]])

    def test_profile_url_path_contains_username_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_path_contains_username"]])

    def test_profile_url_path_contains_username_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com/test",
            "expanded_url": "http://www.test.com/test",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_path_contains_username"]])

    def test_profile_url_path_contains_username_False_3(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test_account.com/test",
            "expanded_url": "http://www.test_account.com/test",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_path_contains_username"]])

    def test_profile_url_path_contains_username_True_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com/test/test_account",
            "expanded_url": "http://www.test.com/test/test_account",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_path_contains_username"]])

    def test_profile_url_path_contains_username_True_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com/test/testaccount",
            "expanded_url": "http://www.test.com/test/testaccount",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_path_contains_username"]])

    def test_profile_url_path_contains_name_False_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_path_contains_name"]])

    def test_profile_url_path_contains_name_False_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://www.test.com",
            "expanded_url": "http://www.test.com",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_path_contains_name"]])

    def test_profile_url_path_contains_name_False_3(self):
        user_dic = {
            "id": 1,
            "name": "test_account",
            "screen_name": "test_username",
            "location": "",
            "url": "http://www.test_account.com",
            "expanded_url": "http://www.test_account.com",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["profile_url_path_contains_name"]])

    def test_profile_url_path_contains_name_True_1(self):
        user_dic = {
            "id": 1,
            "name": "test_account",
            "screen_name": "test_username",
            "location": "",
            "url": "http://www.test.com/test/test_account",
            "expanded_url": "http://www.test.com/test/test_account",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_path_contains_name"]])

    def test_profile_url_path_contains_name_True_2(self):
        user_dic = {
            "id": 1,
            "name": "test account",
            "screen_name": "test_username",
            "location": "",
            "url": "http://www.test.com/test/test_account",
            "expanded_url": "http://www.test.com/test/test_account",
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["profile_url_path_contains_name"]])

    def test_default_profile_img_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["default_profile_img"]])

    def test_default_profile_img_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": False,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["default_profile_img"]])

    def test_default_profile_background_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["default_profile_background"]])

    def test_default_profile_background_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": False,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["default_profile_background"]])

    def test_account_age_days_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-03 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["account_age_days"]], 2)

    def test_account_age_days_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["account_age_days"]], 0)

    def test_number_of_tweets(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_tweets"]], 9)

    def test_number_of_followers(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_followers"]], 10)

    def test_number_of_following(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_following"]], 15)

    def test_number_of_lists(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_lists"]], 2)

    def test_number_of_likes(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["number_of_likes"]], 50)

    def test_protected_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["protected"]])

    def test_protected_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": True,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["protected"]])

    def test_verified_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["verified"]])

    def test_verified_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": True,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["verified"]])

    def test_account_location_provided_False(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertFalse(user_features[USER_FEATURES_INDEX["account_location_provided"]])

    def test_account_location_provided_True(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "Test city",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertTrue(user_features[USER_FEATURES_INDEX["account_location_provided"]])

    def test_account_age_vs_tweets_ratio_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-05 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["account_age_vs_tweets_ratio"]], 4 / 9)

    def test_account_age_vs_tweets_ratio_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 0,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-02 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertEqual(user_features[USER_FEATURES_INDEX["account_age_vs_tweets_ratio"]], 0)

    def test_follower_vs_following_ratio(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["follower_vs_following_ratio"]], 10 / 15)

    def test_tweets_vs_favorites_ratio(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": None,
            "expanded_url": None,
            "description": "",
            "protected": False,
            "verified": False,
            "followers_count": 10,
            "friends_count": 15,
            "listed_count": 2,
            "favourites_count": 50,
            "statuses_count": 9,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "profile_image_url_https": "",
            "default_profile": True,
            "default_profile_image": True,
            "withheld_in_countries": "",
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }
        user = User.parse(api=None, json=user_dic)

        user_features = UserFeatures(user, [])

        self.assertAlmostEqual(user_features[USER_FEATURES_INDEX["tweets_vs_favorites_ratio"]], 9 / 50)


if __name__ == '__main__':
    unittest.main()
