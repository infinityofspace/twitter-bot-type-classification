from datetime import datetime
from urllib.parse import urlsplit

import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from twitter_bot_type_classification.features.tweet import TweetFeatures, LANG_CODES_IDX, TWEET_FEATURES_INDEX, \
    N_FEATURES, \
    TWEET_TEXT_SIMILARITY_FEATURES
from twitter_bot_type_classification.features.utils import URL_REGEX, USERNAME_REGEX, BOT_IN_DIFFERENT_LANG, \
    EMOJI_REGEX, SERVICE_PROFILES, \
    get_expanded_url, TWITTER_URL_SHORTER_REGEX, USERNAME_STRUCTURE_REGEXS

# download punkt sentence tokenizer model
nltk.download("punkt", quiet=True)

USER_FEATURES_INDEX = {
    "tweet_time_interval_mean": 0,
    "tweet_time_interval_std": 1,
    "tweet_likes_mean": 2,
    "tweet_likes_std": 3,
    "tweet_likes_max": 4,
    "tweet_likes_min": 5,
    "tweet_retweets_mean": 6,
    "tweet_retweets_std": 7,
    "tweet_retweets_max": 8,
    "tweet_retweets_min": 9,
    "self_replies_mean": 10,
    "number_of_different_countries": 11,
    "country_with_most_tweets": 12,
    "number_of_different_sources": 13,
    "most_used_source": 14,
    "retweet_tweets_mean": 15,
    "answer_tweets_mean": 16,
    "number_of_withheld_countries_max": 17,
    "withheld_country_tweets_mean": 18,
    "number_of_different_tweet_coord_groups": 19,
    "most_frequent_tweet_coord_group": 20,
    "different_user_interactions": 21,
    "tweet_text_length_max": 22,
    "tweet_text_length_min": 23,
    "tweet_text_length_mean": 24,
    "tweet_text_length_std": 25,
    "number_of_hashtags_max": 26,
    "number_of_hashtags_min": 27,
    "number_of_hashtags_mean": 28,
    "number_of_hashtags_std": 29,
    "length_of_hashtag_grand_mean": 30,
    "length_of_hashtag_max": 31,
    "length_of_hashtag_min": 32,
    "cleaned_tweet_text_length_max": 33,
    "cleaned_tweet_text_length_min": 34,
    "cleaned_tweet_text_length_mean": 35,
    "cleaned_tweet_text_length_std": 36,
    "number_of_user_mentions_mean": 37,
    "number_of_user_mentions_std": 38,
    "number_of_user_mentions_max": 39,
    "number_of_user_mentions_min": 40,
    "number_of_sentences_mean": 41,
    "number_of_sentences_std": 42,
    "number_of_words_mean": 43,
    "number_of_words_std": 44,
    "number_of_emojis_mean": 45,
    "number_of_emojis_std": 46,
    "number_of_emojis_max": 47,
    "number_of_emojis_min": 48,
    "emoji_only_tweets_mean": 49,
    "number_of_tweet_languages": 50,
    "most_used_tweet_language": 51,
    "pagination_tweets_mean": 52,
    "own_tweets_text_similarity_mean": 53,
    "own_tweets_text_similarity_std": 54,
    "retweet_tweets_text_similarity_mean": 55,
    "retweet_tweets_text_similarity_std": 56,
    "number_of_url_mean": 57,
    "number_of_url_std": 58,
    "total_urls_vs_urls_domain_matches_username_ratio": 59,
    "total_urls_vs_total_profile_url_domain_matches_ratio": 60,
    "total_urls_vs_total_other_shortened_urls_ratio": 61,
    "tweets_with_only_urls_mean": 62,
    "number_of_photos_mean": 63,
    "number_of_photos_std": 64,
    "number_of_videos_mean": 65,
    "number_of_videos_std": 66,
    "number_of_gifs_mean": 67,
    "number_of_gifs_std": 68,
    "number_of_user_mentions_in_description": 69,
    "number_description_urls": 70,
    "description_url_contains_username": 71,
    "description_url_contains_name": 72,
    "description_length": 73,
    "number_of_numbers_in_description": 74,
    "number_of_emojis_in_description": 75,
    "description_contains_bot": 76,
    "username_length": 77,
    "username_contains_name": 78,
    "number_of_char_numbers_in_username": 79,
    "username_structure": 80,
    "username_contains_bot": 81,
    "name_length": 82,
    "number_of_numbers_in_name": 83,
    "number_of_emojis_in_name": 84,
    "name_contains_bot": 85,
    "profile_url_to_other_service_profile": 86,
    "profile_url_domain_contains_username": 87,
    "profile_url_domain_contains_name": 88,
    "profile_url_path_contains_username": 89,
    "profile_url_path_contains_name": 90,
    "default_profile_img": 91,
    "default_profile_background": 92,
    "account_age_days": 93,
    "number_of_tweets": 94,
    "number_of_followers": 95,
    "number_of_following": 96,
    "number_of_lists": 97,
    "number_of_likes": 98,
    "protected": 99,
    "verified": 100,
    "account_location_provided": 101,
    "account_age_vs_tweets_ratio": 102,
    "follower_vs_following_ratio": 103,
    "tweets_vs_favorites_ratio": 104
}

TWEETS_ONLY_FEATURES = [
    "tweet_time_interval_mean",
    "tweet_time_interval_std",
    "tweet_likes_mean",
    "tweet_likes_std",
    "tweet_likes_max",
    "tweet_likes_min",
    "tweet_retweets_mean",
    "tweet_retweets_std",
    "tweet_retweets_max",
    "tweet_retweets_min",
    "self_replies_mean",
    "number_of_different_countries",
    "country_with_most_tweets",
    "number_of_different_sources",
    "most_used_source",
    "retweet_tweets_mean",
    "answer_tweets_mean",
    "number_of_withheld_countries_max",
    "withheld_country_tweets_mean",
    "number_of_different_tweet_coord_groups",
    "most_frequent_tweet_coord_group",
    "different_user_interactions",
    "tweet_text_length_max",
    "tweet_text_length_min",
    "tweet_text_length_mean",
    "tweet_text_length_std",
    "number_of_hashtags_max",
    "number_of_hashtags_min",
    "number_of_hashtags_mean",
    "number_of_hashtags_std",
    "length_of_hashtag_grand_mean",
    "length_of_hashtag_max",
    "length_of_hashtag_min",
    "cleaned_tweet_text_length_max",
    "cleaned_tweet_text_length_min",
    "cleaned_tweet_text_length_mean",
    "cleaned_tweet_text_length_std",
    "number_of_user_mentions_mean",
    "number_of_user_mentions_std",
    "number_of_user_mentions_max",
    "number_of_user_mentions_min",
    "number_of_sentences_mean",
    "number_of_sentences_std",
    "number_of_words_mean",
    "number_of_words_std",
    "number_of_emojis_mean",
    "number_of_emojis_std",
    "number_of_emojis_max",
    "number_of_emojis_min",
    "emoji_only_tweets_mean",
    "number_of_tweet_languages",
    "most_used_tweet_language",
    "pagination_tweets_mean",
    "own_tweets_text_similarity_mean",
    "own_tweets_text_similarity_std",
    "retweet_tweets_text_similarity_mean",
    "retweet_tweets_text_similarity_std",
    "number_of_url_mean",
    "number_of_url_std",
    "tweets_with_only_urls_mean",
    "number_of_photos_mean",
    "number_of_photos_std",
    "number_of_videos_mean",
    "number_of_videos_std",
    "number_of_gifs_mean",
    "number_of_gifs_std"
]

TWEETS_ONLY_FEATURES_IDX = [USER_FEATURES_INDEX[f_name] for f_name in TWEETS_ONLY_FEATURES]

USER_ONLY_FEATURES = [
    "number_of_user_mentions_in_description",
    "number_description_urls",
    "description_url_contains_username",
    "description_url_contains_name",
    "description_length",
    "number_of_numbers_in_description",
    "number_of_emojis_in_description",
    "description_contains_bot",
    "username_length",
    "username_contains_name",
    "number_of_char_numbers_in_username",
    "username_structure",
    "username_contains_bot",
    "name_length",
    "number_of_numbers_in_name",
    "number_of_emojis_in_name",
    "name_contains_bot",
    "profile_url_to_other_service_profile",
    "profile_url_domain_contains_username",
    "profile_url_domain_contains_name",
    "profile_url_path_contains_username",
    "profile_url_path_contains_name",
    "default_profile_img",
    "default_profile_background",
    "account_age_days",
    "number_of_tweets",
    "number_of_followers",
    "number_of_following",
    "number_of_lists",
    "number_of_likes",
    "protected",
    "verified",
    "account_location_provided",
    "account_age_vs_tweets_ratio",
    "follower_vs_following_ratio",
    "tweets_vs_favorites_ratio"
]

USER_ONLY_FEATURES_IDX = [USER_FEATURES_INDEX[f_name] for f_name in USER_ONLY_FEATURES]


class UserFeatures(np.ndarray):

    def __new__(cls, user, tweets):
        """
        Generate all user features.

        :param user: user tweepy object
        :param tweets: list of tweepy tweet objects. NOTE: the tweets have to be chronological sorted.

        :return: numpy 1 dim array with all calculated user features
        """

        ### selected tweets features ###

        number_of_selected_tweets = len(tweets)
        if number_of_selected_tweets > 0:
            time_diff_vec = np.zeros((number_of_selected_tweets - 1, 1), dtype=np.int32)
            last_timestamp = None
            tweets_features = np.empty((len(tweets), N_FEATURES), dtype=np.float32)

            interaction_user_ids = set()

            for i, t in enumerate(tweets):
                timestamp = int(t.created_at.timestamp())
                if last_timestamp is not None:
                    time_diff_vec[i - 1] = last_timestamp - timestamp
                last_timestamp = timestamp
                t_features = TweetFeatures(t, user)
                tweets_features[i] = t_features
                if hasattr(t, "in_reply_to_user_id") and t.in_reply_to_user_id is not None:
                    interaction_user_ids.add(t.in_reply_to_user_id)

            different_user_interactions = len(interaction_user_ids)
            tweets_features_mean = np.mean(tweets_features, axis=0)
            tweets_features_std = np.std(tweets_features, axis=0)
            tweets_features_sum = np.sum(tweets_features, axis=0)
            tweets_features_max = np.max(tweets_features, axis=0)
            tweets_features_min = np.min(tweets_features, axis=0)

            # tweet metadata features #
            tweet_time_interval_mean = np.nan if number_of_selected_tweets < 2 else np.nanmean(time_diff_vec)
            tweet_time_interval_std = np.nan if number_of_selected_tweets < 2 else np.std(time_diff_vec)

            tweet_likes_mean = tweets_features_mean[TWEET_FEATURES_INDEX["likes_count"]]
            tweet_likes_std = tweets_features_std[TWEET_FEATURES_INDEX["likes_count"]]
            tweet_likes_max = tweets_features_max[TWEET_FEATURES_INDEX["likes_count"]]
            tweet_likes_min = tweets_features_min[TWEET_FEATURES_INDEX["likes_count"]]

            tweet_retweets_mean = tweets_features_mean[TWEET_FEATURES_INDEX["retweet_count"]]
            tweet_retweets_std = tweets_features_std[TWEET_FEATURES_INDEX["retweet_count"]]
            tweet_retweets_max = tweets_features_max[TWEET_FEATURES_INDEX["retweet_count"]]
            tweet_retweets_min = tweets_features_min[TWEET_FEATURES_INDEX["retweet_count"]]

            self_replies_mean = tweets_features_mean[TWEET_FEATURES_INDEX["is_self_reply"]]

            number_of_different_countries = \
                np.unique(tweets_features[:, TWEET_FEATURES_INDEX["country_code_encoded"]], axis=0).shape[0]

            countries, country_freqs = np.unique(tweets_features[:, TWEET_FEATURES_INDEX["country_code_encoded"]],
                                                 return_counts=True)
            country_with_most_tweets = countries[country_freqs.argmax()]

            number_of_different_sources = \
                np.unique(tweets_features[:, TWEET_FEATURES_INDEX["source_encoded"]], axis=0).shape[
                    0]

            sources, sources_freqs = np.unique(tweets_features[:, TWEET_FEATURES_INDEX["source_encoded"]],
                                               return_counts=True)
            most_used_source = sources[sources_freqs.argmax()]

            retweet_tweets_mean = tweets_features_mean[TWEET_FEATURES_INDEX["is_retweet"]]

            answer_tweets_mean = tweets_features_mean[TWEET_FEATURES_INDEX["is_answer"]]

            number_of_withheld_countries_max = tweets_features_max[TWEET_FEATURES_INDEX["number_of_withheld_countries"]]

            withheld_country_tweets_mean = np.mean(
                tweets_features[:, TWEET_FEATURES_INDEX["number_of_withheld_countries"]] > 0)

            coord_groups, coord_group_freqs = np.unique(tweets_features[:, TWEET_FEATURES_INDEX["coordinates_group"]],
                                                        return_counts=True)
            number_of_different_tweet_coord_groups = len(coord_groups)
            most_frequent_tweet_coord_group = coord_groups[coord_group_freqs.argmax()]

            # tweet text content features #

            tweet_text_length_max = tweets_features_max[TWEET_FEATURES_INDEX["tweet_text_length"]]
            tweet_text_length_min = tweets_features_min[TWEET_FEATURES_INDEX["tweet_text_length"]]
            tweet_text_length_mean = tweets_features_mean[TWEET_FEATURES_INDEX["tweet_text_length"]]
            tweet_text_length_std = tweets_features_std[TWEET_FEATURES_INDEX["tweet_text_length"]]

            number_of_hashtags_max = tweets_features_max[TWEET_FEATURES_INDEX["number_of_hashtags"]]
            number_of_hashtags_min = tweets_features_min[TWEET_FEATURES_INDEX["number_of_hashtags"]]
            number_of_hashtags_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_hashtags"]]
            number_of_hashtags_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_hashtags"]]

            length_of_hashtag_grand_mean = tweets_features_mean[TWEET_FEATURES_INDEX["mean_hashtag_length"]]
            length_of_hashtag_max = tweets_features_max[TWEET_FEATURES_INDEX["max_hashtag_length"]]
            length_of_hashtag_min = tweets_features_min[TWEET_FEATURES_INDEX["min_hashtag_length"]]

            cleaned_tweet_text_length_max = tweets_features_max[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]]
            cleaned_tweet_text_length_min = tweets_features_min[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]]
            cleaned_tweet_text_length_mean = tweets_features_mean[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]]
            cleaned_tweet_text_length_std = tweets_features_std[TWEET_FEATURES_INDEX["cleaned_tweet_text_length"]]

            number_of_user_mentions_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_user_mentions"]]
            number_of_user_mentions_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_user_mentions"]]
            number_of_user_mentions_max = tweets_features_max[TWEET_FEATURES_INDEX["number_of_user_mentions"]]
            number_of_user_mentions_min = tweets_features_min[TWEET_FEATURES_INDEX["number_of_user_mentions"]]

            number_of_sentences_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_sentences"]]
            number_of_sentences_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_sentences"]]

            number_of_words_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_words"]]
            number_of_words_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_words"]]

            number_of_emojis_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_emojis"]]
            number_of_emojis_std = tweets_features_std[TWEET_FEATURES_INDEX["number_emojis"]]
            number_of_emojis_max = tweets_features_max[TWEET_FEATURES_INDEX["number_emojis"]]
            number_of_emojis_min = tweets_features_min[TWEET_FEATURES_INDEX["number_emojis"]]

            emoji_only_tweets_mean = tweets_features_mean[TWEET_FEATURES_INDEX["contains_only_emojis"]]

            number_of_tweet_languages = np.count_nonzero(
                np.unique(tweets_features[:, TWEET_FEATURES_INDEX["lang_encoded"]], axis=0) != LANG_CODES_IDX["und"])

            langs, langs_freqs = np.unique(tweets_features[:, TWEET_FEATURES_INDEX["lang_encoded"]],
                                           return_counts=True)
            most_used_tweet_language = langs[langs_freqs.argmax()]

            pagination_tweets_mean = tweets_features_mean[TWEET_FEATURES_INDEX["contains_pagination"]]

            own_tweets_features = tweets_features[tweets_features[:, TWEET_FEATURES_INDEX["is_retweet"]] == 0]

            if own_tweets_features.shape[0] > 1:
                own_tweets_similarity = cosine_similarity(own_tweets_features[:, TWEET_TEXT_SIMILARITY_FEATURES])
                own_tweets_text_similarity_mean = own_tweets_similarity.mean()
                own_tweets_text_similarity_std = own_tweets_similarity.std()
            else:
                own_tweets_text_similarity_mean = -1.0
                own_tweets_text_similarity_std = -1.0

            retweet_tweet_features = tweets_features[tweets_features[:, TWEET_FEATURES_INDEX["is_retweet"]] == 1]

            if retweet_tweet_features.shape[0] > 1:
                retweet_tweets_similarities = cosine_similarity(
                    retweet_tweet_features[:, TWEET_TEXT_SIMILARITY_FEATURES])
                retweet_tweets_text_similarity_mean = retweet_tweets_similarities.mean()
                retweet_tweets_text_similarity_std = retweet_tweets_similarities.std()
            else:
                retweet_tweets_text_similarity_mean = -1.0
                retweet_tweets_text_similarity_std = -1.0

            # tweet urls content features #

            number_of_url_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_urls"]]
            number_of_url_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_urls"]]

            total_number_of_urls = tweets_features_sum[TWEET_FEATURES_INDEX["number_of_urls"]]

            total_urls_vs_urls_domain_matches_username_ratio = 0
            total_number_of_url_domains_matches_username = tweets_features_sum[
                TWEET_FEATURES_INDEX["number_of_url_domains_matches_username"]]
            if total_number_of_url_domains_matches_username != 0:
                total_urls_vs_urls_domain_matches_username_ratio = total_number_of_urls / total_number_of_url_domains_matches_username

            total_urls_vs_total_profile_url_domain_matches_ratio = 0
            total_number_of_profile_url_domain_matches = tweets_features_sum[
                TWEET_FEATURES_INDEX["number_of_url_domains_matches_profile_url_domain"]]
            if total_number_of_profile_url_domain_matches != 0:
                total_urls_vs_total_profile_url_domain_matches_ratio = total_number_of_urls / total_number_of_profile_url_domain_matches

            total_urls_vs_total_other_shortened_urls_ratio = 0
            total_number_of_other_shortened_urls = tweets_features_sum[
                TWEET_FEATURES_INDEX["number_of_other_shortened_urls"]]
            if total_number_of_other_shortened_urls != 0:
                total_urls_vs_total_other_shortened_urls_ratio = total_number_of_urls / total_number_of_other_shortened_urls

            tweets_with_only_urls_mean = tweets_features_mean[TWEET_FEATURES_INDEX["contains_only_urls"]]

            # tweet photo content features #

            number_of_photos_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_photos"]]
            number_of_photos_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_photos"]]

            # tweet video content features #

            number_of_videos_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_videos"]]
            number_of_videos_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_videos"]]

            # tweet gifs content features #

            number_of_gifs_mean = tweets_features_mean[TWEET_FEATURES_INDEX["number_of_gifs"]]
            number_of_gifs_std = tweets_features_std[TWEET_FEATURES_INDEX["number_of_gifs"]]

        else:
            # set all tweet based features as nan
            tweet_time_interval_mean = np.nan
            tweet_time_interval_std = np.nan
            tweet_likes_mean = np.nan
            tweet_likes_std = np.nan
            tweet_likes_max = np.nan
            tweet_likes_min = np.nan
            tweet_retweets_mean = np.nan
            tweet_retweets_std = np.nan
            tweet_retweets_max = np.nan
            tweet_retweets_min = np.nan
            self_replies_mean = np.nan
            number_of_different_countries = np.nan
            country_with_most_tweets = np.nan
            number_of_different_sources = np.nan
            most_used_source = np.nan
            retweet_tweets_mean = np.nan
            answer_tweets_mean = np.nan
            number_of_withheld_countries_max = np.nan
            withheld_country_tweets_mean = np.nan
            number_of_different_tweet_coord_groups = np.nan
            most_frequent_tweet_coord_group = np.nan
            tweet_text_length_max = np.nan
            tweet_text_length_min = np.nan
            tweet_text_length_mean = np.nan
            tweet_text_length_std = np.nan
            number_of_hashtags_max = np.nan
            number_of_hashtags_min = np.nan
            number_of_hashtags_mean = np.nan
            number_of_hashtags_std = np.nan
            length_of_hashtag_grand_mean = np.nan
            length_of_hashtag_max = np.nan
            length_of_hashtag_min = np.nan
            cleaned_tweet_text_length_max = np.nan
            cleaned_tweet_text_length_min = np.nan
            cleaned_tweet_text_length_mean = np.nan
            cleaned_tweet_text_length_std = np.nan
            number_of_user_mentions_mean = np.nan
            number_of_user_mentions_std = np.nan
            number_of_user_mentions_max = np.nan
            number_of_user_mentions_min = np.nan
            number_of_sentences_mean = np.nan
            number_of_sentences_std = np.nan
            number_of_words_mean = np.nan
            number_of_words_std = np.nan
            number_of_emojis_mean = np.nan
            number_of_emojis_std = np.nan
            number_of_emojis_max = np.nan
            number_of_emojis_min = np.nan
            emoji_only_tweets_mean = np.nan
            number_of_tweet_languages = np.nan
            most_used_tweet_language = np.nan
            pagination_tweets_mean = np.nan
            own_tweets_text_similarity_mean = np.nan
            own_tweets_text_similarity_std = np.nan
            retweet_tweets_text_similarity_mean = np.nan
            retweet_tweets_text_similarity_std = np.nan
            number_of_url_mean = np.nan
            number_of_url_std = np.nan
            total_urls_vs_urls_domain_matches_username_ratio = np.nan
            total_urls_vs_total_profile_url_domain_matches_ratio = np.nan
            total_urls_vs_total_other_shortened_urls_ratio = np.nan
            tweets_with_only_urls_mean = np.nan
            number_of_photos_mean = np.nan
            number_of_photos_std = np.nan
            number_of_videos_mean = np.nan
            number_of_videos_std = np.nan
            number_of_gifs_mean = np.nan
            number_of_gifs_std = np.nan
            different_user_interactions = np.nan

        #### profile description features ####

        user_mentions = USERNAME_REGEX.findall(user.description)
        number_of_user_mentions_in_description = len(user_mentions)

        description_urls = URL_REGEX.findall(user.description)
        number_description_urls = len(description_urls)

        description_url_contains_username = 0
        description_url_contains_name = 0

        username_lower = user.screen_name.lower()
        name_lower = user.name.lower()

        for url, *other in description_urls:
            url_lower = url.lower()
            if int(username_lower in url_lower) \
                    or int(username_lower.replace("_", "") in url_lower) \
                    or int(username_lower.replace("_", "-") in url_lower):
                description_url_contains_username = 1
            if int(name_lower in url_lower) \
                    or int(name_lower.replace(" ", "") in url_lower) \
                    or int(name_lower.replace(" ", "_") in url_lower) \
                    or int(name_lower.replace(" ", "-") in url_lower):
                description_url_contains_name = 1

        description_length = len(user.description)

        description_words_tokenized = nltk.word_tokenize(user.description)
        number_of_numbers_in_description = len(list(
            filter(lambda w: w.isdigit() or w.replace(".", "").replace(",", "").isdigit(),
                   description_words_tokenized)))

        number_of_emojis_in_description = len(EMOJI_REGEX.findall(user.description))

        description_contains_bot = int(any(bot in user.description for bot in BOT_IN_DIFFERENT_LANG))

        ### username features ###

        username_length = len(user.screen_name)

        username_lower = user.screen_name.lower()
        name_lower = user.name.lower()
        username_contains_name = int(name_lower in username_lower) \
                                 or int(name_lower.replace(" ", "") in username_lower) \
                                 or int(name_lower.replace(" ", "_") in username_lower)

        number_of_char_numbers_in_username = sum(char.isdigit() for char in user.screen_name)

        username_structure = -1
        for i, regex in enumerate(USERNAME_STRUCTURE_REGEXS):
            if regex.fullmatch(user.screen_name):
                username_structure = i
                break

        # username consists of alphanumeric characters + underscore
        username_contains_bot = int("bot" in user.screen_name)

        ### name features ###

        name_length = len(user.name)

        number_of_numbers_in_name = sum(char.isdigit() for char in user.name)

        number_of_emojis_in_name = len(EMOJI_REGEX.findall(user.name))

        name_contains_bot = int(any(bot in user.name for bot in BOT_IN_DIFFERENT_LANG))

        ### profile url features ###

        if user.url != "" and user.url is not None:

            if TWITTER_URL_SHORTER_REGEX.match(user.url):
                expanded_profile_url = getattr(user, "expanded_url", None)
                if expanded_profile_url is None:
                    expanded_profile_url = get_expanded_url(user.url)
            else:
                expanded_profile_url = user.url

            profile_url_to_other_service_profile = 0
            if expanded_profile_url != "":
                for service, regex in SERVICE_PROFILES:
                    if regex.match(expanded_profile_url):
                        profile_url_to_other_service_profile = service
                        break

            profile_url = urlsplit(expanded_profile_url)

            username_lower = user.screen_name.lower()
            name_lower = user.name.lower()
            url_netloc_lower = profile_url.netloc.lower()
            url_path_lower = profile_url.path.lower()

            profile_url_domain_contains_username = int(username_lower in url_netloc_lower) \
                                                   or int(username_lower.replace("_", "") in url_netloc_lower) \
                                                   or int(username_lower.replace("_", "-") in url_netloc_lower)
            profile_url_domain_contains_name = int(name_lower in url_netloc_lower) \
                                               or int(name_lower.replace(" ", "") in url_netloc_lower) \
                                               or int(name_lower.replace(" ", "_") in url_netloc_lower) \
                                               or int(name_lower.replace(" ", "-") in url_netloc_lower)

            profile_url_path_contains_username = int(username_lower in url_path_lower) \
                                                 or int(username_lower.replace("_", "") in url_path_lower) \
                                                 or int(username_lower.replace("_", "-") in url_path_lower)
            profile_url_path_contains_name = int(name_lower in url_path_lower) \
                                             or int(name_lower.replace(" ", "") in url_path_lower) \
                                             or int(name_lower.replace(" ", "_") in url_path_lower) \
                                             or int(name_lower.replace(" ", "-") in url_path_lower)

        else:
            profile_url_to_other_service_profile = 0

            profile_url_domain_contains_username = 0
            profile_url_domain_contains_name = 0

            profile_url_path_contains_username = 0
            profile_url_path_contains_name = 0

        ### profile pictures features ###

        default_profile_img = int(user.default_profile_image)

        default_profile_background = int(user.default_profile)

        ### other metadata features ###

        account_age_days = (getattr(user, "fetch_date", datetime.now()) - user.created_at).days

        number_of_tweets = user.statuses_count

        number_of_followers = user.followers_count

        number_of_following = user.friends_count

        number_of_lists = user.listed_count

        number_of_likes = user.favourites_count

        protected = int(user.protected)

        verified = int(user.verified)

        account_location_provided = int(user.location != "")

        account_age_vs_tweets_ratio = 0 if user.statuses_count == 0 else account_age_days / user.statuses_count

        follower_vs_following_ratio = 0 if user.friends_count == 0 else user.followers_count / user.friends_count

        tweets_vs_favorites_ratio = 0 if user.favourites_count == 0 else user.statuses_count / user.favourites_count

        obj = np.asarray([
            ################################
            ### selected tweets features ###
            ################################

            ## tweet metadata features ##

            # mean of tweet time interval between each tweet
            tweet_time_interval_mean,

            # std of tweet time interval between each tweet
            tweet_time_interval_std,

            # tweet likes mean
            tweet_likes_mean,

            # tweet likes std
            tweet_likes_std,

            # max number of likes on one tweet
            tweet_likes_max,

            # min number of likes on one tweet
            tweet_likes_min,

            # tweet retweets mean
            tweet_retweets_mean,

            # tweet retweets std
            tweet_retweets_std,

            # max number of retweets on one tweets
            tweet_retweets_max,

            # min number of retweets on one tweets
            tweet_retweets_min,

            # mean number of self replies
            self_replies_mean,

            # number of different countries
            number_of_different_countries,

            # country with most tweets,
            country_with_most_tweets,

            # number of different sources
            number_of_different_sources,

            # most used source
            most_used_source,

            # mean of tweets which are retweets
            retweet_tweets_mean,

            # mean of tweets which are answers
            answer_tweets_mean,

            # max number of withheld countries
            number_of_withheld_countries_max,

            # mean of tweets which are withheld in any country
            withheld_country_tweets_mean,

            # number of different groups where tweets are posted
            number_of_different_tweet_coord_groups,

            # the coordinate group with the most tweets
            most_frequent_tweet_coord_group,

            # number of different users interacted with with user
            different_user_interactions,

            ## tweet text content features ##

            # longest text length
            tweet_text_length_max,

            # shortest text length
            tweet_text_length_min,

            # tweet text length mean
            tweet_text_length_mean,

            # tweet text length std
            tweet_text_length_std,

            # max number of hashtags in one tweet
            number_of_hashtags_max,

            # min number of hashtags in one tweet
            number_of_hashtags_min,

            # number of hashtag mean
            number_of_hashtags_mean,

            # number of hashtag std
            number_of_hashtags_std,

            # mean of hashtag length means (grand mean)
            length_of_hashtag_grand_mean,

            # max length of one hashtag
            length_of_hashtag_max,

            # min length of one hashtag
            length_of_hashtag_min,

            # max cleaned tweet text length
            cleaned_tweet_text_length_max,

            # min cleaned tweet text length
            cleaned_tweet_text_length_min,

            # cleaned tweet text length mean
            cleaned_tweet_text_length_mean,

            # cleaned tweet text length std
            cleaned_tweet_text_length_std,

            # number of user mentions mean
            number_of_user_mentions_mean,

            # number of user mentions std
            number_of_user_mentions_std,

            # number of user mentions max
            number_of_user_mentions_max,

            # number of user mentions min
            number_of_user_mentions_min,

            # number of sentences per tweet mean
            number_of_sentences_mean,

            # number of sentences per tweet std
            number_of_sentences_std,

            # number of words per tweet mean
            number_of_words_mean,

            # number of words per tweet std
            number_of_words_std,

            # number of emojis mean
            number_of_emojis_mean,

            # number of emojis std
            number_of_emojis_std,

            # number of emojis max
            number_of_emojis_max,

            # number of emojis min
            number_of_emojis_min,

            # mean of tweets which only contains emojis
            emoji_only_tweets_mean,

            # number of different tweet text languages
            number_of_tweet_languages,

            # most used tweet language
            most_used_tweet_language,

            # mean of the number of tweets with pagination
            pagination_tweets_mean,

            # tweet text similarity mean of own tweets
            own_tweets_text_similarity_mean,

            # tweet text similarity std of own tweets
            own_tweets_text_similarity_std,

            retweet_tweets_text_similarity_mean,

            retweet_tweets_text_similarity_std,

            ## tweet urls content features ##

            # tweets url mean
            number_of_url_mean,

            # tweets url std
            number_of_url_std,

            # total #urls / #url domain matches username:
            total_urls_vs_urls_domain_matches_username_ratio,

            # : tweets #urls / domain matches profile url domain / tweets ratio
            total_urls_vs_total_profile_url_domain_matches_ratio,

            # : total #url / shortened #url ratio
            total_urls_vs_total_other_shortened_urls_ratio,

            # tweets with only urls mean
            tweets_with_only_urls_mean,

            ## tweet photo content features ##

            # tweet photos mean
            number_of_photos_mean,

            # number of photos std
            number_of_photos_std,

            ## tweet video content features ##

            # tweet photos mean
            number_of_videos_mean,

            # number of photos std
            number_of_videos_std,

            ## tweet gifs content features ##

            # number of gifs mean
            number_of_gifs_mean,

            # number of gifs std
            number_of_gifs_std,

            ######################################
            #### profile description features ####
            ######################################

            # number of "@" to other account
            number_of_user_mentions_in_description,

            # number of links
            number_description_urls,

            # links contains username
            description_url_contains_username,

            # links contains name
            description_url_contains_name,

            # length of description (chars)
            description_length,

            # number of numbers
            number_of_numbers_in_description,

            # number of emojis
            number_of_emojis_in_description,

            # description contains "bot"
            description_contains_bot,

            #########################
            ### username features ###
            #########################

            # length
            username_length,

            # contains name
            username_contains_name,

            # number of char which are numbers
            number_of_char_numbers_in_username,

            # follows structure (eg. name<number>, <number>name, ...)
            username_structure,

            # username contains "bot"
            username_contains_bot,

            #####################
            ### name features ###
            #####################

            # name length
            name_length,

            # number of numbers in name
            number_of_numbers_in_name,

            # number emojis in name
            number_of_emojis_in_name,

            # name contains "bot"
            name_contains_bot,

            ############################
            ### profile url features ###
            ############################

            # links to other service profiles
            profile_url_to_other_service_profile,

            # url domain contains username
            profile_url_domain_contains_username,

            # url domain contains name
            profile_url_domain_contains_name,

            # url path contains username
            profile_url_path_contains_username,

            # url path contains name
            profile_url_path_contains_name,

            #################################
            ### profile pictures features ###
            #################################

            # default profile image
            default_profile_img,

            # default profile background
            default_profile_background,

            ###############################
            ### other metadata features ###
            ###############################

            # account age in days
            account_age_days,

            # total number of tweets
            number_of_tweets,

            # follower count
            number_of_followers,

            # following count
            number_of_following,

            # lists count
            number_of_lists,

            # likes count
            number_of_likes,

            # account is private
            protected,

            # account verified
            verified,

            # account location
            account_location_provided,

            # account age (days) / tweets ratio
            account_age_vs_tweets_ratio,

            # followers / following ratio
            follower_vs_following_ratio,

            # tweets / favorites ratio
            tweets_vs_favorites_ratio

        ], dtype=np.float32).view(cls)

        return obj
