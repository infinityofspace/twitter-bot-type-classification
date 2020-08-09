import re
import string
from urllib.parse import urlsplit
from xml.sax.saxutils import unescape

import nltk
import numpy as np

from twitter_bot_type_classification.features.utils import URL_SHORTER_REGEX, URL_REGEX, EMOJI_REGEX, HASHTAG_REGEX, \
    USERNAME_REGEX, NUMBER_CHAR_REGEX, \
    get_expanded_url, URL_PATH_SPLIT, COORDINATE_GROUPS, HTML_ESCAPE_TABLE

# download punkt sentence tokenizer model
nltk.download("punkt", quiet=True)  # , download_dir=)

TEXT_ENCODING = "UTF-8"

PAGINATION_START_REGEX = re.compile(r"(^(\d+/\d+)|(?<=^\()\d+/\d+(?=\)))(?![.,]\d)")

PAGINATION_END_REGEX = re.compile(r"(?<!\d[.,])((\d+/\d+)\Z|(?<=\()\d+/\d+(?=\)\Z))")

# ISO 639 1 Language codes
# The following changes have been made in comparison to ISO-639-1:
# "iw" for Hebrew, "ckb" for Kurdish and "in" for Indonesian was added
LANG_CODES_IDX = {
    "ab": 1, "aa": 2, "af": 3, "ak": 4, "sq": 5, "am": 6, "ar": 7, "an": 8, "hy": 9, "as": 10, "av": 11, "ae": 12,
    "ay": 13, "az": 14, "bm": 15, "ba": 16, "eu": 17, "be": 18, "bn": 19, "bh": 20, "bi": 21, "bs": 22, "br": 23,
    "bg": 24, "my": 25, "ca": 26, "ch": 27, "ce": 28, "ny": 29, "zh": 30, "cv": 31, "kw": 32, "co": 33, "cr": 34,
    "hr": 35, "cs": 36, "da": 37, "dv": 38, "nl": 39, "dz": 40, "en": 41, "eo": 42, "et": 43, "ee": 44, "fo": 45,
    "fj": 46, "fi": 47, "fr": 48, "ff": 49, "gl": 50, "ka": 51, "de": 52, "el": 53, "gn": 54, "gu": 55, "ht": 56,
    "ha": 57, "he": 58, "hz": 59, "hi": 60, "ho": 61, "hu": 62, "ia": 63, "id": 64, "ie": 65, "ga": 66, "ig": 67,
    "ik": 68, "io": 69, "is": 70, "it": 71, "iu": 72, "ja": 73, "jv": 74, "kl": 75, "kn": 76, "kr": 77, "ks": 78,
    "kk": 79, "km": 80, "ki": 81, "rw": 82, "ky": 83, "kv": 84, "kg": 85, "ko": 86, "ku": 87, "kj": 88, "la": 89,
    "lb": 90, "lg": 91, "li": 92, "ln": 93, "lo": 94, "lt": 95, "lu": 96, "lv": 97, "gv": 98, "mk": 99, "mg": 100,
    "ms": 101, "ml": 102, "mt": 103, "mi": 104, "mr": 105, "mh": 106, "mn": 107, "na": 108, "nv": 109, "nd": 110,
    "ne": 111, "ng": 112, "nb": 113, "nn": 114, "no": 115, "ii": 116, "nr": 117, "oc": 118, "oj": 119, "cu": 120,
    "om": 121, "or": 122, "os": 123, "pa": 124, "pi": 125, "fa": 126, "pl": 127, "ps": 128, "pt": 129, "qu": 130,
    "rm": 131, "rn": 132, "ro": 133, "ru": 134, "sa": 135, "sc": 136, "sd": 137, "se": 138, "sm": 139, "sg": 140,
    "sr": 141, "gd": 142, "sn": 143, "si": 144, "sk": 145, "sl": 146, "so": 147, "st": 148, "es": 149, "su": 150,
    "sw": 151, "ss": 152, "sv": 153, "ta": 154, "te": 155, "tg": 156, "th": 157, "ti": 158, "bo": 159, "tk": 160,
    "tl": 161, "tn": 162, "to": 163, "tr": 164, "ts": 165, "tt": 166, "tw": 167, "ty": 168, "ug": 169, "uk": 170,
    "ur": 171, "uz": 172, "ve": 173, "vi": 174, "vo": 175, "wa": 176, "cy": 177, "wo": 178, "fy": 179, "xh": 180,
    "yi": 181, "yo": 182, "za": 183, "zu": 184, "in": 185, "iw": 186, "ckb": 187, "und": 188
}

TWEET_SOURCES_IDX = {
    "web": 1,
    "Twitter Web App": 2,
    "Twitter for Android": 3,
    "Twitter for Android Tablets": 4,
    "Twitter for iPhone": 5,
    "Twitter for iPad": 6,
    "Twitter for Mac": 7,
    "Twitter for BlackBerry®": 8,
    "Twitter for BlackBerry": 9,
    "Twitter for Windows": 10,
    "Twitter for Windows Phone": 11,
    "Twitter for Websites": 12,
    "Twitter for Google TV": 13,
    "TweetDeck": 14,
    "": 15  # empty source
}

TWEET_CUSTOM_SOURCES_IDX = {
    "url": 16,
    "other": 17
}

# ISO 3166-1 alpha-2 codes for countries in tweets
# https://developer.twitter.com/en/docs/tutorials/filtering-tweets-by-location
# Note: the temporary country code for Kosovo (XK) was added
COUNTRY_CODES_IDX = {
    "AD": 1, "AE": 2, "AF": 3, "AG": 4, "AI": 5, "AL": 6, "AM": 7, "AO": 8, "AQ": 9, "AR": 10, "AS": 11, "AT": 12,
    "AU": 13, "AW": 14, "AX": 15, "AZ": 16, "BA": 17, "BB": 18, "BD": 19, "BE": 20, "BF": 21, "BG": 22, "BH": 23,
    "BI": 24, "BJ": 25, "BL": 26, "BM": 27, "BN": 28, "BO": 29, "BQ": 30, "BR": 31, "BS": 32, "BT": 33, "BV": 34,
    "BW": 35, "BY": 36, "BZ": 37, "CA": 38, "CC": 39, "CD": 40, "CF": 41, "CG": 42, "CH": 43, "CI": 44, "CK": 45,
    "CL": 46, "CM": 47, "CN": 48, "CO": 49, "CR": 50, "CU": 51, "CV": 52, "CW": 53, "CX": 54, "CY": 55, "CZ": 56,
    "DE": 57, "DJ": 58, "DK": 59, "DM": 60, "DO": 61, "DZ": 62, "EC": 63, "EE": 64, "EG": 65, "EH": 66, "ER": 67,
    "ES": 68, "ET": 69, "FI": 70, "FJ": 71, "FK": 72, "FM": 73, "FO": 74, "FR": 75, "GA": 76, "GB": 77, "GD": 78,
    "GE": 79, "GF": 80, "GG": 81, "GH": 82, "GI": 83, "GL": 84, "GM": 85, "GN": 86, "GP": 87, "GQ": 88, "GR": 89,
    "GS": 90, "GT": 91, "GU": 92, "GW": 93, "GY": 94, "HK": 95, "HM": 96, "HN": 97, "HR": 98, "HT": 99, "HU": 100,
    "ID": 101, "IE": 102, "IL": 103, "IM": 104, "IN": 105, "IO": 106, "IQ": 107, "IR": 108, "IS": 109, "IT": 110,
    "JE": 111, "JM": 112, "JO": 113, "JP": 114, "KE": 115, "KG": 116, "KH": 117, "KI": 118, "KM": 119, "KN": 120,
    "KP": 121, "KR": 122, "KW": 123, "KY": 124, "KZ": 125, "LA": 126, "LB": 127, "LC": 128, "LI": 129, "LK": 130,
    "LR": 131, "LS": 132, "LT": 133, "LU": 134, "LV": 135, "LY": 136, "MA": 137, "MC": 138, "MD": 139, "ME": 140,
    "MF": 141, "MG": 142, "MH": 143, "MK": 144, "ML": 145, "MM": 146, "MN": 147, "MO": 148, "MP": 149, "MQ": 150,
    "MR": 151, "MS": 152, "MT": 153, "MU": 154, "MV": 155, "MW": 156, "MX": 157, "MY": 158, "MZ": 159, "NA": 160,
    "NC": 161, "NE": 162, "NF": 163, "NG": 164, "NI": 165, "NL": 166, "NO": 167, "NP": 168, "NR": 169, "NU": 170,
    "NZ": 171, "OM": 172, "PA": 173, "PE": 174, "PF": 175, "PG": 176, "PH": 177, "PK": 178, "PL": 179, "PM": 180,
    "PN": 181, "PR": 182, "PS": 183, "PT": 184, "PW": 185, "PY": 186, "QA": 187, "RE": 188, "RO": 189, "RS": 190,
    "RU": 191, "RW": 192, "SA": 193, "SB": 194, "SC": 195, "SD": 196, "SE": 197, "SG": 198, "SH": 199, "SI": 200,
    "SJ": 201, "SK": 202, "SL": 203, "SM": 204, "SN": 205, "SO": 206, "SR": 207, "SS": 208, "ST": 209, "SV": 210,
    "SX": 211, "SY": 212, "SZ": 213, "TC": 214, "TD": 215, "TF": 216, "TG": 217, "TH": 218, "TJ": 219, "TK": 220,
    "TL": 221, "TM": 222, "TN": 223, "TO": 224, "TR": 225, "TT": 226, "TV": 227, "TW": 228, "TZ": 229, "UA": 230,
    "UG": 231, "UM": 232, "US": 233, "UY": 234, "UZ": 235, "VA": 236, "VC": 237, "VE": 238, "VG": 239, "VI": 240,
    "VN": 241, "VU": 242, "WF": 243, "WS": 244, "YE": 245, "YT": 246, "ZA": 247, "ZM": 248, "ZW": 249, "XK": 250
}

COUNTRY_CODES_IDX_UNDEF = 0

TWEET_TEXT_SIMILARITY_FEATURES = list(range(14, 43))

TWEET_FEATURES_INDEX = {
    "retweet_count": 0,
    "likes_count": 1,
    "coordinates_group": 2,
    "country_code_encoded": 3,
    "source_encoded": 4,
    "is_retweet": 5,
    "is_answer": 6,
    "is_self_reply": 7,
    "contains_quote": 8,
    "number_of_withheld_countries": 9,
    "lang_encoded": 10,
    "number_of_photos": 11,
    "number_of_videos": 12,
    "number_of_gifs": 13,
    "contains_pagination": 14,
    "contains_only_emojis": 15,
    "contains_only_urls": 16,
    "number_of_urls": 17,
    "number_of_other_shortened_urls": 18,
    "number_of_url_domains_matches_username": 19,
    "number_of_url_domains_matches_profile_url_domain": 20,
    "number_of_urls_matches_tweet_text": 21,
    "number_of_hashtags": 22,
    "mean_hashtag_length": 23,
    "max_hashtag_length": 24,
    "min_hashtag_length": 25,
    "number_of_user_mentions": 26,
    "number_of_sentences": 27,
    "mean_sentence_length": 28,
    "number_of_numbers": 29,
    "max_number_length": 30,
    "min_number_length": 31,
    "max_word_length": 32,
    "min_word_length": 33,
    "number_of_words": 34,
    "mean_number_of_words_per_sentences": 35,
    "max_number_of_words_per_sentences": 36,
    "min_number_of_words_per_sentences": 37,
    "number_of_punctuations": 38,
    "number_of_uppercase_words": 39,
    "cleaned_tweet_text_length": 40,
    "tweet_text_length": 41,
    "number_emojis": 42
}

N_FEATURES = len(TWEET_FEATURES_INDEX)


class TweetFeatures(np.ndarray):

    def __new__(cls, tweet, user):
        """
        Calculate all tweet features and return as a numpy vector

        :param tweet: tweepy tweet object
        :param user: tweepy user object

        :return: numpy 1 dim vector with all calculated tweet features
        """

        #### tweet metadata features ####

        likes_count = 0 if getattr(tweet, "favorite_count", None) is None else tweet.favorite_count

        # longitude (-180 to 180), latitude (-90 to 90)
        coordinates_group = -1
        if tweet.coordinates is not None:
            coords = tweet.coordinates.get("coordinates", [])
            if len(coords) > 1:
                coordinates_group = len(COORDINATE_GROUPS)
                for i, paths in enumerate(COORDINATE_GROUPS):
                    if coordinates_group != len(COORDINATE_GROUPS):
                        break
                    for path in paths:
                        if path.contains_point(coords[:2], radius=-1e-8):
                            coordinates_group = i
                            break

        country_code_encoded = COUNTRY_CODES_IDX_UNDEF
        place = tweet.place
        if place is not None:
            country_code_encoded = COUNTRY_CODES_IDX.get(place.country_code, COUNTRY_CODES_IDX_UNDEF)

        source_encoded = TWEET_SOURCES_IDX.get(tweet.source, None)
        if source_encoded is None:
            if URL_REGEX.match(tweet.source):
                source_encoded = TWEET_CUSTOM_SOURCES_IDX["url"]
            else:
                source_encoded = TWEET_CUSTOM_SOURCES_IDX["other"]

        is_retweet = int(getattr(tweet, "retweeted_status", None) is not None)

        is_answer = int(getattr(tweet, "in_reply_to_status_id", None) is not None)

        is_self_reply = int(tweet.in_reply_to_user_id == user.id)

        contains_quote = int(getattr(tweet, "quoted_status_id", None) is not None)

        if hasattr(tweet, "withheld_in_countries"):
            number_of_withheld_countries = 0 if tweet.withheld_in_countries is None else len(
                tweet.withheld_in_countries)
        else:
            number_of_withheld_countries = 0

        #### tweet content features ####

        tweet_text_length = len(tweet.text)

        # check if the links were shortened by a service other than Twitter
        other_shortened_urls = URL_SHORTER_REGEX.findall(tweet.text)
        number_of_other_shortened_urls = len(other_shortened_urls)

        number_of_photos = 0
        number_of_videos = 0
        number_of_gifs = 0
        if hasattr(tweet, "photos") and hasattr(tweet, "videos") and hasattr(tweet, "gifs"):
            # this data is only present when loading from dataset, is this case the entities attribute contains only urls
            number_of_photos = tweet.photos
            number_of_videos = tweet.videos
            number_of_gifs = tweet.gifs
        else:
            # get number of media contents in the tweet
            for media in tweet.entities.get("media", []):
                if media["type"] == "photo":
                    number_of_photos += 1
                elif media["type"] == "video":
                    number_of_videos += 1
                elif media["type"] == "animated_gif":
                    number_of_gifs += 1

        expanded_urls = []
        cleaned_tweet_text = tweet.text
        # unescape the html entities in the tweet text, for example &gt; as >
        cleaned_tweet_text = unescape(cleaned_tweet_text, HTML_ESCAPE_TABLE)

        for url in tweet.entities["urls"]:
            cleaned_tweet_text = cleaned_tweet_text.replace(url["url"], "")
            expanded_url = url["expanded_url"]
            if expanded_url in other_shortened_urls:
                expanded_url = get_expanded_url(expanded_url)
            expanded_urls.append(expanded_url)

        # contains urls which are not found by twitter api
        regex_urls = []

        for m in URL_REGEX.finditer(cleaned_tweet_text):
            url = m.group()
            if url in other_shortened_urls:
                url = get_expanded_url(url)
            regex_urls.append(url)
            cleaned_tweet_text = cleaned_tweet_text.replace(m[0], "")

        cleaned_tweet_text, number_emojis = EMOJI_REGEX.subn("", cleaned_tweet_text)

        words_tokenized = nltk.word_tokenize(cleaned_tweet_text)
        words = list(filter(lambda w: w not in string.punctuation, words_tokenized))

        expanded_urls = expanded_urls + regex_urls

        number_of_urls = len(expanded_urls)

        contains_only_urls = number_of_urls > 0 and len(
            cleaned_tweet_text.replace(" ", "")) == 0 and number_emojis == 0 and len(tweet.text) != 0

        number_of_url_domains_matches_username = 0
        number_of_url_domains_matches_profile_url_domain = 0
        number_of_urls_matches_tweet_text = 0

        profile_url = getattr(user, "expanded_url", user.url)

        for url in expanded_urls:
            url_split = urlsplit(url)
            hostname = url_split.hostname
            if hostname is None:
                # if the url is without a scheme
                hostname = url.split("/", 1)[0]

            if user.screen_name.lower() in hostname.lower():
                number_of_url_domains_matches_username += 1
            if profile_url is not None and hostname.lower() in profile_url.lower():
                number_of_url_domains_matches_profile_url_domain += 1

            url_splits = list(filter(None, URL_PATH_SPLIT.split(url_split.path.lower())))
            for w in words:
                if w.lower() in url_splits:
                    number_of_urls_matches_tweet_text += 1
                    break

        contains_only_emojis = number_emojis > 0 and len(
            cleaned_tweet_text.replace(" ", "")) == 0 and number_of_urls == 0 and len(tweet.text) != 0

        lang_encoded = LANG_CODES_IDX[tweet.lang]

        number_of_words = len(words)

        max_word_length = 0
        min_word_length = 0
        number_of_uppercase_words = 0
        for word in words:
            word_length = len(word)
            if max_word_length < word_length:
                max_word_length = word_length
            if min_word_length > word_length or min_word_length == 0:
                min_word_length = word_length
            lowercase_letter = False
            for letter in word:
                if letter.islower():
                    lowercase_letter = True

            if not lowercase_letter:
                number_of_uppercase_words += 1

        cleaned_tweet_text_length = len(cleaned_tweet_text)

        hashtags = HASHTAG_REGEX.findall(cleaned_tweet_text)
        number_of_hashtags = len(hashtags)
        max_hashtag_length = 0
        min_hashtag_length = 0
        hashtag_lengths = []
        for hashtag in hashtags:
            hashtag_length = len(hashtag)
            hashtag_lengths.append(hashtag_length)
            if max_hashtag_length < hashtag_length:
                max_hashtag_length = hashtag_length
            if min_hashtag_length > hashtag_length or min_hashtag_length == 0:
                min_hashtag_length = hashtag_length

        if not hashtag_lengths:
            mean_hashtag_length = 0
        else:
            mean_hashtag_length = np.mean(hashtag_lengths)

        user_mentions = USERNAME_REGEX.findall(cleaned_tweet_text)
        number_of_user_mentions = len(user_mentions)

        numbers = NUMBER_CHAR_REGEX.findall(cleaned_tweet_text)
        number_of_numbers = len(numbers)
        max_number_length = 0
        min_number_length = 0
        for number in numbers:
            number_length = len(number.replace(".", "").replace(",", ""))
            if max_number_length < number_length:
                max_number_length = number_length
            if min_number_length > number_length or min_number_length == 0:
                min_number_length = number_length

        start_paginations = PAGINATION_START_REGEX.findall(cleaned_tweet_text)
        if len(start_paginations) == 1:
            c_page, t_pages = start_paginations[0][0].split("/")
            contains_start_pagination = int(int(c_page) <= int(t_pages))
        else:
            contains_start_pagination = 0

        end_paginations = PAGINATION_END_REGEX.findall(cleaned_tweet_text)
        if len(end_paginations) == 1:
            c_page, t_pages = end_paginations[0][0].split("/")
            contains_end_pagination = int(int(c_page) <= int(t_pages))
        else:
            contains_end_pagination = 0

        contains_pagination = int(contains_start_pagination != contains_end_pagination)

        sentences = nltk.sent_tokenize(cleaned_tweet_text)
        number_of_sentences = len(sentences)

        number_of_punctuations = 0
        sentences_lengths = []
        words_per_sentences = []
        for s in sentences:
            sentences_lengths.append(len(s))
            words = nltk.word_tokenize(s)
            filtered_words = []
            for w in words:
                if w not in string.punctuation:
                    filtered_words.append(w)
                else:
                    number_of_punctuations += 1

            words_per_sentences.append(len(filtered_words))

        if not sentences_lengths:
            mean_sentence_length = 0
        else:
            mean_sentence_length = np.mean(sentences_lengths)

        if not words_per_sentences:
            mean_number_of_words_per_sentences = 0
        else:
            mean_number_of_words_per_sentences = np.mean(words_per_sentences)

        max_number_of_words_per_sentences = 0 if len(words_per_sentences) == 0 else max(words_per_sentences)
        min_number_of_words_per_sentences = 0 if len(words_per_sentences) == 0 else min(words_per_sentences)

        #### tweet metadata features ####

        obj = np.asarray([
            #### tweet metadata features ####

            # number of times this tweet has been retweeted
            tweet.retweet_count,

            # number of times this tweet has been liked
            likes_count,

            # tweet coordinates group
            coordinates_group,

            # country code
            country_code_encoded,

            # tweet source
            source_encoded,

            # is retweet
            is_retweet,

            # is answer
            is_answer,

            # is self reply
            is_self_reply,

            # contains quote
            contains_quote,

            # number of countries where the tweet is withheld
            number_of_withheld_countries,

            #### tweet content features ####

            # language code encoded
            lang_encoded,

            # number photos
            number_of_photos,

            # number videos
            number_of_videos,

            # number videos
            number_of_gifs,

            # text contains tweet pagination (tweet start or ends with "y/x")
            contains_pagination,

            # tweet contains only emojis and no other text
            contains_only_emojis,

            # tweet contains only urls and no other text
            contains_only_urls,

            # number of urls in the tweet
            number_of_urls,

            # number shortened urls of other services than Twitter
            number_of_other_shortened_urls,

            # number of url domains in the tweet matches the username
            number_of_url_domains_matches_username,

            # number of url domains in the tweet matches the profile url domain
            number_of_url_domains_matches_profile_url_domain,

            # number of urls which contains parts of the tweets text
            number_of_urls_matches_tweet_text,

            # number hashtags
            number_of_hashtags,

            # mean hashtag length
            mean_hashtag_length,

            # max hashtag length
            max_hashtag_length,

            # min hashtag length
            min_hashtag_length,

            # number user mentions with '@'
            number_of_user_mentions,

            # number of sentences
            number_of_sentences,

            # mean sentence length
            mean_sentence_length,

            # number of numbers
            number_of_numbers,

            # max number length
            max_number_length,

            # min number length
            min_number_length,

            # max word length
            max_word_length,

            # min word length
            min_word_length,

            # number of words
            number_of_words,

            # mean number of words per sentence
            mean_number_of_words_per_sentences,

            # max number of words per sentence
            max_number_of_words_per_sentences,

            # min number of words per sentence
            min_number_of_words_per_sentences,

            # number of punctuations !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
            number_of_punctuations,

            # number of CAPS words
            number_of_uppercase_words,

            # cleaned text length (chars)
            cleaned_tweet_text_length,

            # tweet text length (not cleaned)
            tweet_text_length,

            # number of emojis in the tweet text
            number_emojis

        ], dtype=np.float32).view(cls)

        return obj
