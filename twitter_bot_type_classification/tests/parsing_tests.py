import unittest
from datetime import datetime

from twitter_bot_type_classification.dataset.db import DATE_TIME_FORMAT, UserDB, TweetDB


class ParsingTests(unittest.TestCase):

    def test_parse_user_user_id(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.id, 123456789)

    def test_parse_user_name_1(self):
        """
        Text only name
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.name, "Test Name")

    def test_parse_user_name_2(self):
        """
        Text and emojis name
        """
        row = ["123456789", "Test Name \\U0001f600", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.name, "Test Name 😀")

    def test_parse_user_username_1(self):
        """
        Username text only
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.screen_name, "test_username")

    def test_parse_user_username_2(self):
        """
        Username with numbers
        """
        row = ["123456789", "Test Name", "test_username123", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.screen_name, "test_username123")

    def test_parse_user_location(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.location, "Test Location")

    def test_parse_user_url(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.url, "http://t.co/123456")

    def test_parse_user_expanded_url(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.expanded_url, "https://twitter.com")

    def test_parse_user_description_1(self):
        """
        Text only description
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning.",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.description, "This is a simple profile description with no meaning.")

    def test_parse_user_description_2(self):
        """
        Emojis and text description
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.description,
                         "This is a simple profile description with no meaning. 😀")

    def test_parse_user_protected_False(self):
        """
        Protected False
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertFalse(user.protected)

    def test_parse_user_protected_True(self):
        """
        Protected True
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "True", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertTrue(user.protected)

    def test_parse_user_verified_False(self):
        """
        Verified False
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertFalse(user.verified)

    def test_parse_user_verified_True(self):
        """
        Verified True
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "True", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertTrue(user.verified)

    def test_parse_user_followers_count(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.followers_count, 123)

    def test_parse_user_friends_count(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.friends_count, 567)

    def test_parse_user_listed_count(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.listed_count, 8910)

    def test_parse_user_favourites_count(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.favourites_count, 111213)

    def test_parse_user_statuses_count(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.statuses_count, 141516)

    def test_parse_user_created_at(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.created_at, datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT))

    def test_parse_user_profile_image_url_https(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.profile_image_url_https, "http://t.co/profile_img")

    def test_parse_user_default_profile_False(self):
        """
        Default profile background image False         
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertFalse(user.default_profile)

    def test_parse_user_default_profile_True(self):
        """
        Default profile background image True         
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "True", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertTrue(user.default_profile)

    def test_parse_user_default_profile_image_False(self):
        """
        Default profile image False         
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertFalse(user.default_profile_image)

    def test_parse_user_default_profile_image_True(self):
        """
        Default profile image True         
        """
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "True", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertTrue(user.default_profile_image)

    def test_parse_user_withheld_in_countries_empty(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.withheld_in_countries, None)

    def test_parse_user_withheld_in_countries_not_empty(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "en;de;fr", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.withheld_in_countries, ["en", "de", "fr"])

    def test_parse_user_list_separator(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "en/de/fr", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator="/")
        self.assertEqual(user.withheld_in_countries, ["en", "de", "fr"])

    def test_parse_user_fetch_date(self):
        row = ["123456789", "Test Name", "test_username", "Test Location", "http://t.co/123456",
               "https://twitter.com",
               "This is a simple profile description with no meaning. \\U0001f600",
               "False", "False", "123", "567", "8910", "111213", "141516", "2000-01-01 00:00:00",
               "http://t.co/profile_img", "False", "False", "", "2000-01-01 23:59:59"]
        user = UserDB.parse_user(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(user.fetch_date, datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT))

    def test_parse_tweet_id(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "", "", "",
            "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.id, 1234)

    def test_parse_tweet_user_id(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "", "", "",
            "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.user_id, 5647)

    def test_parse_tweet_created_at(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "", "", "",
            "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.created_at, datetime.strptime("2000-01-01 00:00:00", DATE_TIME_FORMAT))

    def test_parse_tweet_text_1(self):
        """
        Only text
        """
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "", "", "",
            "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.text, "This is just a simple tweet text.")

    def test_parse_tweet_text_2(self):
        """
        Emojis and text
        """
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "\\U0001f600 This is just a simple tweet text. \\U0001f600", "", "",
            "", "", "", "", "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App",
            "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.text, "😀 This is just a simple tweet text. 😀")

    def test_parse_tweet_text_3(self):
        """
        Only Emojis
        """
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "\\U0001f600 \\U0001f600 \\U0001f600", "", "", "", "", "", "", "",
            "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.text, "😀 😀 😀")

    def test_parse_tweet_text_4(self):
        """
        Only one link
        """
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "https://twitter.com", "", "", "", "", "", "", "", "",
            "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.text, "https://twitter.com")

    def test_parse_tweet_text_5(self):
        """
        Emojis, links and text
        """
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "\\U0001f600 This is just a simple tweet text. https://twitter.com",
            "", "", "", "", "", "", "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App",
            "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.text, "😀 This is just a simple tweet text. https://twitter.com")

    def test_parse_tweet_coordinates_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "", "", "",
            "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.coordinates, None)

    def test_parse_tweet_coordinates_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "-12.135;56.78", "", "", "", "",
            "", "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.coordinates["coordinates"], [-12.135, 56.78])

    def test_parse_tweet_country_code_and_place_name_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "", "", "",
            "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.place, None)

    def test_parse_tweet_country_code_and_place_name_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "DE", "Berlin", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.place.country_code, "DE")
        self.assertEqual(tweet.place.name, "Berlin")

    def test_parse_tweet_in_reply_to_status_id_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.in_reply_to_status_id, None)

    def test_parse_tweet_in_reply_to_status_id_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "789", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.in_reply_to_status_id, 789)

    def test_parse_tweet_in_reply_to_user_id_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.in_reply_to_user_id, None)

    def test_parse_tweet_in_reply_to_user_id_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "678", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.in_reply_to_user_id, 678)

    def test_parse_tweet_quoted_status_id_and_quoted_text_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "678", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.quoted_status_id, None)

    def test_parse_tweet_quoted_status_id_and_quoted_text_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "234",
            "This is a quotet text.", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App",
            "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.quoted_status_id, 234)
        self.assertEqual(tweet.quoted_status.text, "This is a quotet text.")

    def test_parse_tweet_retweeted_status_id_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertFalse(hasattr(tweet, "retweeted_status"))

    def test_parse_tweet_retweeted_status_id_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "456", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.retweeted_status.id, 456)

    def test_parse_tweet_retweet_count(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.retweet_count, 2)

    def test_parse_tweet_favorite_count(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.favorite_count, 3)

    def test_parse_tweet_favorite_lang(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.lang, "en")

    def test_parse_tweet_withheld_copyright_False(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertFalse(tweet.withheld_copyright)

    def test_parse_tweet_withheld_copyright_True(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "True", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertTrue(tweet.withheld_copyright)

    def test_parse_tweet_withheld_in_countries_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.withheld_in_countries, None)

    def test_parse_tweet_withheld_in_countries_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "DE;GB;US", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.withheld_in_countries, ["DE", "GB", "US"])

    def test_parse_tweet_urls_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.entities["urls"], [])

    def test_parse_tweet_urls_not_empty(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "",
            "{'http://t.co/test-url-1': 'http://twitter.com/test1', 'http://t.co/test-url-2': 'http://twitter.com/test2'}",
            "4", "5", "6", "Twitter Web App",
            "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.entities["urls"], [{
            "url": "http://t.co/test-url-1",
            "expanded_url": "http://twitter.com/test1"
        }, {
            "url": "http://t.co/test-url-2",
            "expanded_url": "http://twitter.com/test2"
        }, ])

    def test_parse_tweet_videos(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.videos, 4)

    def test_parse_tweet_photos(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.photos, 5)

    def test_parse_tweet_gifs(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.gifs, 6)

    def test_parse_tweet_source(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.source, "Twitter Web App")

    def test_parse_tweet_fetch_date(self):
        row = [
            "1234", "5647", "2000-01-01 00:00:00", "This is just a simple tweet text.", "", "", "", "", "", "",
            "", "", "2", "3", "en", "False", "", "{}", "4", "5", "6", "Twitter Web App", "2000-01-01 23:59:59"
        ]
        tweet = TweetDB.parse_tweet(row=row, file_encoding="utf-8", text_encoding="unicode_escape", list_separator=";")
        self.assertEqual(tweet.fetch_date, datetime.strptime("2000-01-01 23:59:59", DATE_TIME_FORMAT))


if __name__ == '__main__':
    unittest.main()
