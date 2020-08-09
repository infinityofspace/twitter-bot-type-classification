import csv
import importlib
import pathlib
import re
import xml.etree.ElementTree as ET
from datetime import timedelta

import requests
from matplotlib.path import Path

from twitter_bot_type_classification import data

unicode_emojis = []

with importlib.resources.open_text(data, "emoji-test.txt") as f:
    reader = csv.reader(f, delimiter=";")

    for r in reader:
        if len(r) == 0 or "#" in r[0]:
            continue
        unicode_emojis.append(r[0].strip().split(" "))

emojis_escaped = [re.escape("".join(chr(int(e.zfill(8), 16)) for e in emoji)) for emoji in unicode_emojis]

EMOJI_REGEX = re.compile("|".join(emojis_escaped), flags=re.UNICODE)

URL_REGEX = re.compile(
    r"\b((http(s)?://)?((([a-zA-Z]|\d|(?<=([a-zA-Z]|\d))-(?=([a-zA-Z]|\d))))+\.)*(([a-zA-Z]|\d|(?<=([a-zA-Z]|\d))-(?=([a-zA-Z]|\d))))+\.(([a-zA-Z]|(\d+\.\d+\.\d+)))+(:[1-9]\d{0,4})?(\/([a-zA-Z]|\d|(?<=([a-zA-Z]|\d))-(?=([a-zA-Z]|\d)))*)*(([a-zA-Z]|\d)+\?(([a-zA-Z]|\d)+\=([a-zA-Z]|\d|_|-|%)+)+(&([a-zA-Z]|\d)+=([a-zA-Z]|\d|_|-|%)+)*)?(#([a-zA-Z]|\d)*)?)\b")

URL_SHORTER_REGEX = re.compile(
    r"\b(http(s)?://)?(www.)?bit.ly/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?tinyurl.com/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?tiny.cc/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?goo.gl/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?dausel.co/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?git.io/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?is.gd/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?sh.st/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?adfoc.us/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?v.gd/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?s.id/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?ouo.io/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?ow.ly/([A-z]|\d)+\b"
    r"|\b(http(s)?://)?(www.)?qr.ae/([A-z]|\d)+\b")

NUMBER_CHAR_REGEX = re.compile(r"\b\d+,\d+|\d+\.\d+|(?<!\w)\d+(?!\w)\b")

HASHTAG_REGEX = re.compile(r"#\w+")

USERNAME_REGEX = re.compile(r"@([A-z]|\d)+")

USERNAME_STRUCTURE_REGEXS = [
    # 0: <name>
    re.compile(r"^[a-z]+$"),
    # 1: <NAME>
    re.compile(r"^[A-Z]+$"),
    # 2: <nAme>, <NaMe>, <naME>, <NAme>, <name><Name>, <Name>, <Name><Name>
    re.compile(r"^(([A-Z]+[a-z]+)|([a-z]+[A-Z]+)|([a-z]+[A-Z]+[a-z]+))+$"),
    # 3: <number>
    re.compile(r"^\d+$"),
    # 4: <name><number>
    re.compile(r"^[a-z]+\d+$"),
    # 5: <NAME><number>
    re.compile(r"^[A-Z]+\d+$"),
    # 6: <nAmE><number>
    re.compile(r"^(([A-Z]+[a-z]+)|([a-z]+[A-Z]+)|([a-z]+[A-Z]+[a-z]+))+\d+$"),
    # 7: <number><name>
    re.compile(r"^\d+[a-z]+$"),
    # 8: <number><NAME>
    re.compile(r"^\d+[A-Z]+$"),
    # 9: <number><nAmE>
    re.compile(r"^\d+(([A-Z]+[a-z]+)|([a-z]+[A-Z]+)|([a-z]+[A-Z]+[a-z]+))+$"),
    # 10: <number><any-letter><number>, <number><any-letter><number><any-letter>...
    re.compile(r"^((\d+[A-Za-z]+\d+)|(\d+[A-Za-z]+\d+[A-Za-z]+))+$"),
    # 11: <any-letter><number><any-letter>, <any-letter><number><any-letter><number><any-letter>...
    re.compile(r"^(([A-Za-z]+\d+[A-Za-z]+)|([A-Za-z]+\d+[A-Za-z]+\d+))+$"),
    # 12: __<any-letter-or-number>__
    re.compile(r"^__([A-Za-z]|\d)+__$"),
    # 13: <any-letter-or-number>_<any-letter-or-number>, <any-letter-or-number>_<any-letter-or-number>_<any-letter-or-number>
    re.compile(r"^(([A-Za-z]|\d)+_([A-Za-z]|\d)+)+$")
]

BOT_IN_DIFFERENT_LANG = [
    "bot",  # German, English, French, Turkish, Spanish, Portuguese, Polish, Dutch, Italian
    "Бот",  # Russian
    "บอท",  # Thai
    "봇",  # Korean
    "ボット",  # Japanese
    "機器人",  # Chinese-traditional
    "机器人",  # Chinese-simplified
    "بوت"  # Arabic
]

URL_SCHEME = re.compile("(http(s)?)?(: //)?(www.)?")

SERVICE_PROFILES = [
    # Facebook
    (1, re.compile(r"^(http(s)?://)((\w+(-)?\w+)|m)\.facebook\.com/(\w|.)+(/)?\Z")),
    # Reddit
    (2, re.compile(r"^(http(s)?://)?www\.reddit\.com/user/\w+(/)?\Z")),
    # Twitter
    (3, re.compile(r"^(http(s)?://)?((www|m)\.)?twitter\.com/\w+(/)?\Z")),
    # Linkedin
    (4, re.compile(r"^(http(s)?://)?(\w*\.)?linkedin\.com/(in|company)/(\w|-)+(/)?\Z")),
    # VK
    (5, re.compile("^(http(s)?://)?(\w*\.)?vk\.com/\w+(/)?\Z")),
    # Instagram
    (6, re.compile(r"^(http(s)?://)?(www\.)?instagram\.com/(\w|.|-)+(/)?\Z")),
    # Flickr
    (7, re.compile(r"^(http(s)?://)?(www\.)?flickr\.com/people/\w+(/)?\Z")),
    # Xing
    (8, re.compile(r"^(http(s)?://)?(www\.)?xing\.com/profile/\w+(/)?\Z")),
    # About.me
    (9, re.compile(r"^(http(s)?://)?(www\.)?about\.me/\w+(/)?\Z")),
    # Tumblr
    (10, re.compile(r"^(http(s)?://)\w+\.tumblr\.com(/)?\Z")),
    # Pinterest
    (11, re.compile(r"^(http(s)?://)?(www\.)?pinterest\.\w+/\w+(/)?\Z")),
    # Youtube
    (12, re.compile(r"^(http(s)?://)?((www|m)\.)?youtube\.com/(\w+|channel/\w+)\Z"))]

URL_PATH_SPLIT = re.compile("[-._~/]")

COORDINATE_GROUPS = [
    [Path(
        [(-80.9, 31), (-75.5, 35), (-73, 40), (-50.1, 47.8), (-63, 60.3), (-129, 71.5), (-136.3, 69.4), (-157.6, 71.6),
         (-166.5, 68.89), (-168.5, 65.8), (-168.5, 63.5), (-168.3, 62.5), (-168, 60), (-158, 57.5), (-172, 52.8),
         (-180, 52.8), (-180, 51.2), (-166, 52.7), (-153, 56.4), (-147, 60), (-126, 48.5), (-125, 38), (-116, 25),
         (-84, 7), (-78.2, 7.2), (-76.8, 9), (-83, 11), (-83, 16), (-88, 16.5), (-86, 21.8), (-90, 21.8), (-92, 19),
         (-95.8, 19), (-97.5, 24), (-96.5, 28.2), (-84, 29.5), (-82, 23.5), (-85, 22.5), (-85, 21.5), (-80, 17.5),
         (-63.5, 17.5), (-61.5, 14), (-61.9, 11.8), (-59, 13), (-62, 18.8), (-73, 22.6), (-80.9, 31)]),
        Path([(180, 52.8), (175, 52.8), (166, 55.5), (165.5, 55.1), (174.5, 51.5), (180, 51.2), (180, 52.8)])],
    [Path([(-63, 60.3), (-42, 59), (-38, 63), (-13.5, 63), (-9, 81.9), (-31.5, 84), (-60, 82.4), (-65, 83), (-78, 83.3),
           (-123, 77), (-129, 71.5), (-63, 60.3)])],
    [Path([(-76.8, 9), (-75, 11.3), (-70, 13.2), (-60.5, 11), (-58, 7), (-51, 5), (-49, 0), (-33, -5), (-38, -15),
           (-41, -23), (-48, -26), (-48.5, -29), (-69, -51), (-63, -55), (-68, -56.2), (-75.5, -54), (-76, -46),
           (-71, -18.5), (-76.5, -14.5), (-83, -4), (-78, 4), (-78.2, 7.2)]), Path(
        [(-61.3, -50.9), (-57.9, -51.3), (-57.55, -51.65), (-59, -52.6), (-60.8, -52.3), (-61.5, -51.8),
         (-61.3, -50.9)])],
    [Path(
        [(4, 6), (-2, 4.5), (-8, 4.2), (-13.8, 8), (-18.6, 14), (-18, 22), (-6.9, 35.9), (-5, 36), (11, 37.7), (19, 34),
         (34, 31.7), (35, 28), (43.7, 12), (52.3, 12.2), (48, 3.53), (40, -4.5), (41.5, -16), (35, -20), (36, -24.5),
         (33.2, -26), (32.5, -29.5), (27, -34), (20, -34.9), (18.4, -34.4), (17.7, -32.8), (16.9, -29.5), (15.4, -28),
         (12.7, -19.5), (11.2, -17.5), (13, -10), (8.5, -1), (8.3, 2.2), (4, 6)]),
        Path([(49.5, -11.5), (51, -16), (47, -26), (43, -25.2), (43, -17), (49.5, -11.5)])],
    [Path([(-6.9, 35.9), (-5, 36), (11, 37.7), (19, 34), (34, 31.7), (27, 35.5), (25, 40), (29, 41), (36, 45), (40, 49),
           (33, 53), (28, 58), (27.85, 60.6), (31.5, 62.8), (29, 67), (29, 71.1), (25, 71.3), (13, 69), (12.5, 66.3),
           (9, 64), (4.3, 62.3), (5.3, 58.5), (8.5, 57.4), (7.8, 56.5), (8.4, 53.9), (4.5, 53.4), (4, 52), (2, 51.2),
           (1.8, 52.8), (-1.5, 56), (-2, 59.6), (-7.8, 58.4), (-7.8, 55.5), (-11, 54), (-10.5, 51.4), (-6.2, 51.4),
           (-5, 48), (-1.6, 46), (-1.6, 43.5), (-9.5, 43.9), (-9, 40.6), (-10, 37.5), (-6.9, 35.9)])],
    [Path([(131, 42.5), (135, 42.7), (139, 46), (144, 45.8), (147.3, 44), (143, 41), (141, 35), (122, 22), (129, 4),
           (153, -2), (180, -16), (180, -19), (167, -24), (153, -12), (133, -8), (123.2, -11.3), (107, -8), (101, -5),
           (93.5, 6), (98, 6), (97.5, 15.5), (94, 15.5), (92, 21), (88, 21), (82, 16), (80, 11), (82.2, 7.2),
           (81.2, 5.4), (76.8, 8), (72, 18.5), (66, 25), (61.5, 25), (57, 16.5), (43.7, 12), (35, 28), (34, 31.7),
           (27, 35.5), (25, 40), (29, 41), (36, 45), (49, 42), (48, 51), (70, 56), (88, 49), (100, 52), (119, 50),
           (120, 53.5), (126, 53.5), (128, 50), (132, 48), (134.8, 48.5), (131, 42.5)])],
    [Path([(36, 45), (49, 42), (48, 51), (70, 56), (88, 49), (100, 52), (119, 50), (120, 53.5), (126, 53.5), (128, 50),
           (132, 48), (134.8, 48.5), (131, 42.5), (135, 42.7), (139, 46), (144, 45.8), (145, 49), (143, 54.5),
           (139, 55), (138, 56), (143, 59), (158, 58.5), (154.7, 56.5), (155.8, 51.5), (154, 49), (155, 49),
           (163.5, 55.7), (163.5, 58.4), (171, 60), (180, 62.5), (180, 69.5), (178, 70), (115, 75), (114, 76.5),
           (104, 78), (69, 73.5), (55, 69.5), (29, 71.1), (29, 67), (31.5, 62.8), (27.85, 60.6), (28, 58), (33, 53),
           (40, 49), (36, 45)]), Path(
        [(-180, 69.5), (-180, 62.5), (-176, 63.6), (-168.3, 62.5), (-168.5, 63.5), (-172.5, 64.3), (-169.3, 66.1),
         (-171.8, 67), (-180, 69.5)])],
    [Path([(-180, -65), (180, -65), (180, -90), (-180, -90), (-180, -65)])],
    [Path([(165, -46), (174, -38.5), (172.2, -33.8), (179.9, -38.2), (168, -48), (165, -46)])],
    [Path([(115, -36), (112, -23), (130, -10.8), (143, -10.5), (155.5, -27), (148, -45), (131, -33), (115, -36)])]
]

TWITTER_URL_SHORTER_REGEX = re.compile(r"http(s)?://t\.co/.*")

# based on https://data.iana.org/time-zones/releases/tzdata2019c.tar.gz
COUNTRY_TIMEZONE = {'AD': 1, 'AE': 4, 'AF': 4.5, 'AG': -4, 'AI': -4, 'AL': 1, 'AM': 4, 'AO': 1, 'AQ': 6, 'AR': -3,
                    'AS': -11, 'AT': 1, 'AU': 8.75, 'AW': -4, 'AX': 2, 'AZ': 4, 'BA': 1, 'BB': -4, 'BD': 6, 'BE': 1,
                    'BF': 0, 'BG': 2, 'BH': 3, 'BI': 2, 'BJ': 1, 'BL': -4, 'BM': -4, 'BN': 8, 'BO': -4, 'BQ': -4,
                    'BR': -5, 'BS': -5, 'BT': 6, 'BW': 2, 'BY': 3, 'BZ': -6, 'CA': -8, 'CC': 6.5, 'CD': 2, 'CF': 1,
                    'CG': 1, 'CH': 1, 'CI': 0, 'CK': -10, 'CL': -6, 'CM': 1, 'CN': 6, 'CO': -5, 'CR': -6, 'CU': -5,
                    'CV': -1, 'CW': -4, 'CX': 7, 'CY': 2, 'CZ': 1, 'DE': 1, 'DJ': 3, 'DK': 1, 'DM': -4, 'DO': -4,
                    'DZ': 1, 'EC': -6, 'EE': 2, 'EG': 2, 'EH': 1, 'ER': 3, 'ES': 0, 'ET': 3, 'FI': 2, 'FJ': 12,
                    'FK': -3, 'FM': 11, 'FO': 0, 'FR': 1, 'GA': 1, 'GB': 0, 'GD': -4, 'GE': 4, 'GF': -3, 'GG': 0,
                    'GH': 0, 'GI': 1, 'GL': -4, 'GM': 0, 'GN': 0, 'GP': -4, 'GQ': 1, 'GR': 2, 'GS': -2, 'GT': -6,
                    'GU': 10, 'GW': 0, 'GY': -4, 'HK': 8, 'HN': -6, 'HR': 1, 'HT': -5, 'HU': 1, 'ID': 9, 'IE': 0,
                    'IL': 2, 'IM': 0, 'IN': 5.5, 'IO': 6, 'IQ': 3, 'IR': 3.5, 'IS': 0, 'IT': 1, 'JE': 0, 'JM': -5,
                    'JO': 2, 'JP': 9, 'KE': 3, 'KG': 6, 'KH': 7, 'KI': 14, 'KM': 3, 'KN': -4, 'KP': 9, 'KR': 9, 'KW': 3,
                    'KY': -5, 'KZ': 5, 'LA': 7, 'LB': 2, 'LC': -4, 'LI': 1, 'LK': 5.5, 'LR': 0, 'LS': 2, 'LT': 2,
                    'LU': 1, 'LV': 2, 'LY': 2, 'MA': 1, 'MC': 1, 'MD': 2, 'ME': 1, 'MF': -4, 'MG': 3, 'MH': 12, 'MK': 1,
                    'ML': 0, 'MM': 6.5, 'MN': 8, 'MO': 8, 'MP': 10, 'MQ': -4, 'MR': 0, 'MS': -4, 'MT': 1, 'MU': 4,
                    'MV': 5, 'MW': 2, 'MX': -6, 'MY': 8, 'MZ': 2, 'NA': 2, 'NC': 11, 'NE': 1, 'NF': 11, 'NG': 1,
                    'NI': -6, 'NL': 1, 'NO': 1, 'NP': 5.75, 'NR': 12, 'NU': -11, 'NZ': 12.75, 'OM': 4, 'PA': -5,
                    'PE': -5, 'PF': -9, 'PG': 11, 'PH': 8, 'PK': 5, 'PL': 1, 'PM': -3, 'PN': -8, 'PR': -4, 'PS': 2,
                    'PT': -1, 'PW': 9, 'PY': -4, 'QA': 3, 'RE': 4, 'RO': 2, 'RS': 1, 'RU': 12, 'UA': 2, 'RW': 2,
                    'SA': 3, 'SB': 11, 'SC': 4, 'SD': 2, 'SE': 1, 'SG': 8, 'SH': 0, 'SI': 1, 'SJ': 1, 'SK': 1, 'SL': 0,
                    'SM': 1, 'SN': 0, 'SO': 3, 'SR': -3, 'SS': 3, 'ST': 0, 'SV': -6, 'SX': -4, 'SY': 2, 'SZ': 2,
                    'TC': -5, 'TD': 1, 'TF': 5, 'TG': 0, 'TH': 7, 'TJ': 5, 'TK': 13, 'TL': 9, 'TM': 5, 'TN': 1,
                    'TO': 13, 'TR': 3, 'TT': -4, 'TV': 12, 'TW': 8, 'TZ': 3, 'UG': 3, 'UM': 12, 'US': -10, 'UY': -3,
                    'UZ': 5, 'VA': 1, 'VC': -4, 'VE': -4, 'VG': -4, 'VI': -4, 'VN': 7, 'VU': 11, 'WF': 12, 'WS': 13,
                    'YE': 3, 'YT': 3, 'ZA': 2, 'ZM': 2, 'ZW': 2}

# html 5 entities source: https://www.w3.org/2003/entities/2007xml/html5ents.xml
tree = ET.parse(pathlib.Path(__file__).parent.absolute() / "../data/html5ents.xml")
root = tree.getroot()

HTML_ESCAPE_TABLE = {}

for item in root[0][1]:
    unicode = item[1].text.strip()
    entity = "&" + item[0][0].text.lower()
    HTML_ESCAPE_TABLE[entity] = unicode


def get_local_time(dt, offset):
    return dt + timedelta(minutes=offset * 60)


def get_expanded_url(url, timeout=5):
    expanded_url = requests.head(url).headers["location"]

    if URL_SCHEME.sub("", expanded_url) == URL_SCHEME.sub("", url):
        try:
            expanded_url = requests.get(url, timeout=timeout).url
        except requests.exceptions.ConnectionError as e:
            expanded_url = e.request.url
        except requests.exceptions.ReadTimeout as e:
            expanded_url = e.request.url
        except requests.exceptions.TooManyRedirects as e:
            expanded_url = e.request.url

    return expanded_url
