import unittest
from datetime import datetime

from tweepy import Status, User

from features.tweet import TweetFeatures, TWEET_FEATURES_INDEX, LANG_CODES_IDX, TWEET_CUSTOM_SOURCES_IDX, \
    TWEET_SOURCES_IDX
from twitter_bot_type_classification.dataset.db import DATE_TIME_FORMAT, TWITTER_DATE_TIME_FORMAT


class TweetFeaturesTests(unittest.TestCase):
    def test_retweet_count(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["retweet_count"]], 2)

    def test_likes_count(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["likes_count"]], 3)

    def test_coordinates_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], -1)

    def test_coordinates_0(self):
        """
        group 0
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [-102.107469, 42.866337]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 0)

    def test_coordinates_0_1(self):
        """
        group 0
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [172.953048, 52.913415]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 0)

    def test_coordinates_1(self):
        """
        group 1
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [-42.250807, 75.493225]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 1)

    def test_coordinates_2(self):
        """
        group 2
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [-55.494037, -9.798877]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 2)

    def test_coordinates_2_1(self):
        """
        group 2
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [-59.885354, -51.671967]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 2)

    def test_coordinates_3(self):
        """
        group 3
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [4.452179, 24.786907]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 3)

    def test_coordinates_3_1(self):
        """
        group 3
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [46.801725, -18.897898]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 3)

    def test_coordinates_4(self):
        """
        group 4
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [10.340154, 50.956158]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 4)

    def test_coordinates_5(self):
        """
        group 5
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [74.705730, 20.946690]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 5)

    def test_coordinates_6(self):
        """
        group 6
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [83.104288, 62.080373]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 6)

    def test_coordinates_6_1(self):
        """
        group 7
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [-174.565829, 65.788005]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 6)

    def test_coordinates_7(self):
        """
        group 7
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [0, -80]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 7)

    def test_coordinates_8(self):
        """
        group 8
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [169.889812, -44.898769]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 8)

    def test_coordinates_9(self):
        """
        group 9
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [135.526158, -24.490849]
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
        }
        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 9)

    def test_coordinates_10(self):
        """
        not in any group; group 10
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": {
                "coordinates": [-145.856092, -10.324007]
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["coordinates_group"]], 10)

    def test_country_code_encoded_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["country_code_encoded"]], 0.0)

    def test_country_code_encoded_not_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": None,
            "place": {
                "name": "Berlin",
                "country_code": "DE"
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["country_code_encoded"]], 57.0)

    def test_source_encoded_1(self):
        """
        source empty
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
            "source": "",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["source_encoded"]], TWEET_SOURCES_IDX[""])

    def test_source_encoded_2(self):
        """
        source: Twitter Web App
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["source_encoded"]], TWEET_SOURCES_IDX["Twitter Web App"])

    def test_source_encoded_3(self):
        """
        source contains a url
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
            "source": "http://www.twitter.com",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["source_encoded"]], TWEET_CUSTOM_SOURCES_IDX["url"])

    def test_source_encoded_4(self):
        """
        source is something other
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
            "source": "Test Source",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["source_encoded"]], TWEET_CUSTOM_SOURCES_IDX["other"])

    def test_is_retweet_False(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["is_retweet"]], 0.0)

    def test_is_retweet_True(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["is_retweet"]], 1.0)

    def test_is_answer_False(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["is_answer"]], 0.0)

    def test_is_answer_True(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": None,
            "place": None,
            "in_reply_to_status_id": 50,
            "in_reply_to_user_id": 80,
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["is_answer"]], 1.0)

    def test_is_self_reply_False(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["is_self_reply"]], 0.0)

    def test_is_self_reply_True(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": None,
            "place": None,
            "in_reply_to_status_id": 42,
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["is_self_reply"]], 1)

    def test_contains_quote_False(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_quote"]], 0.0)

    def test_contains_quote_True(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": None,
            "place": None,
            "in_reply_to_status_id": None,
            "in_reply_to_user_id": None,
            "quoted_status_id": 67,
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_quote"]], 1.0)

    def test_number_of_withheld_countries_1(self):
        """
        empty
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_withheld_countries"]], 0.0)

    def test_number_of_withheld_countries_2(self):
        """
        one country
        :return:
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
            "withheld_in_countries": ["DE"],
            "entities": {
                "urls": []
            },
            "source": "Twitter Web App",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_withheld_countries"]], 1.0)

    def test_number_of_withheld_countries_3(self):
        """
        two countries
        :return:
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
            "withheld_in_countries": ["DE", "FR"],
            "entities": {
                "urls": []
            },
            "source": "Twitter Web App",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_withheld_countries"]], 2.0)

    def test_tweet_text_length_empty(self):
        """
        empty text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["tweet_text_length"]], 0.0)

    def test_tweet_text_length_not_empty(self):
        """
        not empty text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["tweet_text_length"]],
                         len("This is just a simple test tweet text."))

    def test_number_emojis_1(self):
        """
        no emojis only text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_emojis"]], 0.0)

    def test_number_emojis_2(self):
        """
        one emoji and text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_emojis"]], 1.0)

    def test_number_emojis_3(self):
        """
        two emojis and text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 😀 😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_emojis"]], 2.0)

    def test_number_emojis_4(self):
        """
        empty text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_emojis"]], 0)

    def test_number_emojis_5(self):
        """
        one emoji
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_emojis"]], 1.0)

    def test_contains_only_emojis_only_text(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_emojis"]], 0.0)

    def test_contains_only_emojis_only_emojis(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "😀😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_emojis"]], 1.0)

    def test_contains_only_emojis_only_emojis_with_spaces(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "😀 😀 😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_emojis"]], 1.0)

    def test_contains_only_emojis_empty_text(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_emojis"]], 0.0)

    def test_contains_only_emojis_emojis_and_text(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "😀 This is just a simple test tweet text. 😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_emojis"]], 0.0)

    def test_lang_encoded_undefined(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text.",
            "coordinates": None,
            "place": None,
            "in_reply_to_status_id": None,
            "in_reply_to_user_id": None,
            "quoted_status_id": None,
            "retweet_count": 2,
            "favorite_count": 3,
            "lang": "und",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["lang_encoded"]], LANG_CODES_IDX["und"])

    def test_lang_encoded(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["lang_encoded"]], LANG_CODES_IDX["en"])

    def test_number_of_urls_1(self):
        """
        no urls
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_urls"]], 0.0)

    def test_number_of_urls_2(self):
        """
        one url
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.t.com/abc",
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
                "urls": [
                    {
                        "url": "www.t.com/abc",
                        "expanded_url": "www.testdomain.com"
                    }
                ]
            },
            "source": "Twitter Web App",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_urls"]], 1)

    def test_number_of_urls_3(self):
        """
        two urls
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.t.com/abc www.t.com/ebd",
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
                "urls": [
                    {
                        "url": "www.t.com/abc",
                        "expanded_url": "www.testdomain.com"
                    },
                    {
                        "url": "www.t.com/ebd",
                        "expanded_url": "www.testdomain.com"
                    }
                ]
            },
            "source": "Twitter Web App",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_urls"]], 2.0)

    def test_number_of_urls_4(self):
        """
        url not found by twitter api
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.t.com/abc",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_urls"]], 1.0)

    def test_contains_only_urls_empty(self):
        """
        empty text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_urls"]], 0.0)

    def test_contains_only_urls_1(self):
        """
        only text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_urls"]], 0.0)

    def test_contains_only_urls_2(self):
        """
        one url and text
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.t.com/abc",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_urls"]], 0.0)

    def test_contains_only_urls_3(self):
        """
        two urls
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "www.t.com/abc www.t.com/123",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_urls"]], 1.0)

    def test_contains_only_urls_4(self):
        """
        two urls and one emoji
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "www.t.com/abc www.t.com/123 😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_only_urls"]], 0.0)

    def test_number_of_other_shortened_urls_1(self):
        """
        no urls
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_other_shortened_urls"]], 0)

    def test_number_of_other_shortened_urls_2(self):
        """
        one not shortened url
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.google.de",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_other_shortened_urls"]], 0.0)

    def test_number_of_other_shortened_urls_3(self):
        """
        one other shortened urls
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. bit.ly/abcde",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_other_shortened_urls"]], 1.0)

    def test_number_of_other_shortened_urls_4(self):
        """
        two not different other shortened urls
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. goo.gl/15 goo.gl/15",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_other_shortened_urls"]], 2.0)

    def test_number_of_url_domains_matches_username_1(self):
        """
        no urls
        """
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)
        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_url_domains_matches_username"]], 0.0)

    def test_number_of_url_domains_matches_username_2(self):
        """
        one url and one matches
        """
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "testdomain",
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.t.com/abc",
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
                "urls": [
                    {
                        "url": "www.t.com/abc",
                        "expanded_url": "www.testdomain.com"
                    }
                ]
            },
            "source": "Twitter Web App",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_url_domains_matches_username"]], 1.0)

    def test_number_of_url_domains_matches_username_3(self):
        """
        two urls and one matches
        """
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "testdomain",
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.t.com/abc www.t.com/ebd",
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
                "urls": [
                    {
                        "url": "www.t.com/abc",
                        "expanded_url": "www.testdomain.com"
                    },
                    {
                        "url": "www.t.com/ebd",
                        "expanded_url": "www.otherdomain.com"
                    }
                ]
            },
            "source": "Twitter Web App",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_url_domains_matches_username"]], 1.0)

    def test_number_of_url_domains_matches_username_4(self):
        """
        two urls and two matches
        """
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "testdomain",
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.t.com/abc www.t.com/ebd",
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
                "urls": [
                    {
                        "url": "www.t.com/abc",
                        "expanded_url": "www.testdomain.com"
                    },
                    {
                        "url": "www.t.com/ebd",
                        "expanded_url": "www.testdomain.com"
                    }
                ]
            },
            "source": "Twitter Web App",
            "videos": 0,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_url_domains_matches_username"]], 2.0)

    def test_number_of_url_domains_matches_profile_url_domain__empty(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://t.co/test",
            "expanded_url": "http://www.testdomain.com",
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_url_domains_matches_profile_url_domain"]], 0.0)

    def test_number_of_url_domains_matches_profile_url_domain_1(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://t.co/test",
            "expanded_url": "http://www.testdomain.com",
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. http://www.testdomain.com",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_url_domains_matches_profile_url_domain"]], 1.0)

    def test_number_of_url_domains_matches_profile_url_domain_2(self):
        user_dic = {
            "id": 1,
            "name": "Test Account",
            "screen_name": "test_account",
            "location": "",
            "url": "http://t.co/test",
            "expanded_url": "http://www.testdomain.com",
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. http://www.testdomain.com http://www.testdomain.com/testpath",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_url_domains_matches_profile_url_domain"]], 2.0)

    def test_number_of_photos(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 3/1",
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
            "photos": 7,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_photos"]], 7)

    def test_number_of_videos(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 3/1",
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
            "videos": 8,
            "photos": 0,
            "gifs": 0,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_videos"]], 8)

    def test_number_of_gifs(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 3/1",
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
            "gifs": 4,
            "fetch_date": datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT)
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_gifs"]], 4)

    def test_number_of_hashtags_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_hashtags"]], 0.0)

    def test_number_of_hashtags_not_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. #testhashtag",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_hashtags"]], 1.0)

    def test_max_hashtag_length_no_hashtags(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_hashtag_length"]], 0.0)

    def test_max_hashtag_length(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. #test1 #test2test",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_hashtag_length"]], len("#test2test"))

    def test_min_hashtag_length_no_hashtags(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_hashtag_length"]], 0.0)

    def test_min_hashtag_length(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. #test1 #test2test",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_hashtag_length"]], len("#test1"))

    def test_number_of_user_mentions_no_user_mentions(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_user_mentions"]], 0.0)

    def test_number_of_user_mentions_same_users(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. @test_user @test_user",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_user_mentions"]], 2.0)

    def test_number_of_user_mentions(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. @test_user @abc",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_user_mentions"]], 2.0)

    def test_number_of_sentences_no_text(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_sentences"]], 0)

    def test_number_of_sentences_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_sentences"]], 1.0)

    def test_number_of_sentences_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text, but this is a other sentence. Moreover this is a second sample sentence.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_sentences"]], 2.0)

    def test_mean_sentence_length_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["mean_sentence_length"]], 0.0)

    def test_mean_sentence_length_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["mean_sentence_length"]],
                         len("This is just a simple test tweet text."))

    def test_mean_sentence_length_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. This is another test sentence.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["mean_sentence_length"]],
                         (len("This is just a simple test tweet text.") + len("This is another test sentence.")) / 2)

    def test_number_of_numbers_empty_text(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_numbers"]], 0.0)

    def test_number_of_numbers_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_numbers"]], 0.0)

    def test_number_of_numbers_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 12235",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_numbers"]], 1)

    def test_number_of_numbers_3(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just -1.2567 a simple test tweet text. 12235",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_numbers"]], 2)

    def test_max_number_length_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_number_length"]], 0.0)

    def test_max_number_length_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 12340",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_number_length"]], 5.0)

    def test_max_number_length_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 12.5 1542 45 96",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_number_length"]], 4.0)

    def test_min_number_length_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_number_length"]], 0.0)

    def test_min_number_length_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 9 1.5 1542 453 961",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_number_length"]], 1.0)

    def test_min_number_length_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 1.5 1542 453 961",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_number_length"]], 2.0)

    def test_max_word_length_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_word_length"]], 0.0)

    def test_max_word_length_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_word_length"]], 6.0)

    def test_max_word_length_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple simple test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_word_length"]], 6.0)

    def test_min_word_length_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_word_length"]], 0.0)

    def test_min_word_length_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_word_length"]], 1.0)

    def test_min_word_length_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just second simple test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_word_length"]], 2.0)

    def test_number_of_words_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_words"]], 0.0)

    def test_number_of_words_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_words"]], 8.0)

    def test_number_of_words_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text, 1.5 is a float number.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_words"]], 13.0)

    def test_mean_number_of_words_per_sentences_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["mean_number_of_words_per_sentences"]], 0.0)

    def test_mean_number_of_words_per_sentences_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["mean_number_of_words_per_sentences"]], 8.0)

    def test_mean_number_of_words_per_sentences_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. This is another test sentence.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["mean_number_of_words_per_sentences"]], 6.5)

    def test_max_number_of_words_per_sentences_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_number_of_words_per_sentences"]], 0.0)

    def test_max_number_of_words_per_sentences_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_number_of_words_per_sentences"]], 8.0)

    def test_max_number_of_words_per_sentences_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text, but this is a second test sentence.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_number_of_words_per_sentences"]], 15.0)

    def test_max_number_of_words_per_sentences_3(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. This is a shorter test sentence.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["max_number_of_words_per_sentences"]], 8.0)

    def test_min_number_of_words_per_sentences_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_number_of_words_per_sentences"]], 0.0)

    def test_min_number_of_words_per_sentences_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_number_of_words_per_sentences"]], 8.0)

    def test_min_number_of_words_per_sentences_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text, but this is a second test sentence.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_number_of_words_per_sentences"]], 15.0)

    def test_min_number_of_words_per_sentences_3(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. This is a shorter test sentence.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["min_number_of_words_per_sentences"]], 6.0)

    def test_number_of_punctuations_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_punctuations"]], 0.0)

    def test_number_of_punctuations_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_punctuations"]], 1.0)

    def test_number_of_punctuations_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. This is a second test sentence, but it has no meaning.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_punctuations"]], 3.0)

    def test_number_of_uppercase_words_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_uppercase_words"]], 0)

    def test_number_of_uppercase_words_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. TEST",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_uppercase_words"]], 1.0)

    def test_number_of_uppercase_words_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is CAPS just a simple test tweet text. TEST",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["number_of_uppercase_words"]], 2.0)

    def test_cleaned_tweet_text_length_empty(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]], 0)

    def test_cleaned_tweet_text_length_only_text(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]],
                         len("This is just a simple test tweet text."))

    def test_cleaned_tweet_text_length_text_emojis(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just 😀 a simple test😀 tweet text. 😀 😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]],
                         len("This is just 😀 a simple test😀 tweet text. 😀 😀") - 4)

    def test_cleaned_tweet_text_length_text_emojis_urls(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just 😀 a simple test😀 tweet www.google.de twitter.com/testaccount text. 😀 😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]], len(
            "This is just 😀 a simple test😀 tweet www.google.de twitter.com/testaccount text. 😀 😀") - 4 - len(
            "www.google.de") - len("twitter.com/testaccount"))

    def test_cleaned_tweet_text_length_text_urls(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. www.google.de twitter.com/testaccount",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]],
                         len("This is just a simple test tweet text. www.google.de twitter.com/testaccount") - len(
                             "www.google.de") - len("twitter.com/testaccount"))

    def test_cleaned_tweet_text_length_urls(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "www.google.de twitter.com/testaccount",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]],
                         len("www.google.de twitter.com/testaccount") - len("www.google.de") - len(
                             "twitter.com/testaccount"))

    def test_cleaned_tweet_text_length_emojis(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "😀 😀 😀",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]], len("😀 😀 😀") - 3)

    def test_contains_pagination_1(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_2(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple 1/2 test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_3(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple (1/2) test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_4(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "(1/2) this is just a simple test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 1)

    def test_contains_pagination_5(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "(1/2) this is just a simple test tweet text. (2/2)",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_6(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 1)

    def test_contains_pagination_7(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "1/2 this is just a simple test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 1)

    def test_contains_pagination_8(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 2/2",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 1)

    def test_contains_pagination_9(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "2/1 this is just a simple test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_10(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 3/1",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_11(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "(1.2/2) this is just a simple test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_12(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "1.2/2 this is just a simple test tweet text.",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_13(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. (1.2/2)",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)

    def test_contains_pagination_14(self):
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

        tweet_dic = {
            "id": 0,
            "user_id": 1,
            "created_at": datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT).strftime(TWITTER_DATE_TIME_FORMAT),
            "text": "This is just a simple test tweet text. 1.2/2",
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
        }

        tweet = Status.parse(api=None, json=tweet_dic)

        tweet_features = TweetFeatures(tweet, user)

        self.assertEqual(tweet_features[TWEET_FEATURES_INDEX["contains_pagination"]], 0)


if __name__ == '__main__':
    unittest.main()
