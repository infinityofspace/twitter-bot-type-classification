import argparse
import csv
import textwrap

import tweepy

from twitter_bot_type_classification.dataset.generation import UserDatasetGenerator, \
    TweetDatasetGenerator


def load_csv_file(filename, skip_header=False):
    with open(filename) as f:
        reader = csv.reader(f)

        if skip_header:
            next(reader)

        return [row[0] for row in reader]


def main():
    parser = argparse.ArgumentParser(description="Generate Twitter dataset of tweet and user data.",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent("""\
                                     License:
                                        MIT - Copyright (c) 2020 Marvin Heptner
                                     
                                     Third party notices:
                                        Files:
                                            emoji-test.txt
                                                Project: https://unicode.org/Public/emoji/13.0/emoji-test.txt
                                                License: https://www.unicode.org/license.html
                                            html5ents.xml
                                                Project: https://www.w3.org/2003/entities/2007xml/html5ents.xml
                                                License: https://www.w3.org/Consortium/Legal/2015/doc-license
                                                Notice: Copyright © 2010 World Wide Web Consortium, (MIT, ERCIM, Keio, Beihang). http://www.w3.org/Consortium/Legal/2015/doc-license
                                        Modules:
                                            requests
                                                Project: https://github.com/psf/requests
                                                License: https://github.com/psf/requests/blob/master/LICENSE
                                            numpy
                                                Project: https://github.com/numpy/numpy
                                                License: https://github.com/numpy/numpy/blob/master/LICENSE.txt
                                            tweepy
                                                Project: https://github.com/tweepy/tweepy
                                                License: https://github.com/tweepy/tweepy/blob/master/LICENSE
                                            nltk
                                                Project: https://github.com/nltk/nltk
                                                License: https://github.com/nltk/nltk/blob/develop/LICENSE.txt
                                            tensorflow
                                                Project: https://github.com/tensorflow/tensorflow
                                                License: https://github.com/tensorflow/tensorflow/blob/master/LICENSE
                                            scikit-learn
                                                Project: https://github.com/scikit-learn/scikit-learn
                                                License: https://github.com/scikit-learn/scikit-learn/blob/master/COPYING
                                            botometer
                                                Project: https://github.com/IUNetSci/botometer-python
                                                License: https://github.com/IUNetSci/botometer-python/blob/master/LICENSE.txt
                                            jupyterlab
                                                Project: https://github.com/jupyterlab/jupyterlab
                                                License: https://github.com/jupyterlab/jupyterlab/blob/master/LICENSE
                                            plotly
                                                Project: https://github.com/plotly/plotly.py
                                                License: https://github.com/plotly/plotly.py/blob/master/LICENSE.txt
                                            matplotlib
                                                Project: https://github.com/matplotlib/matplotlib
                                                License: https://matplotlib.org/users/license.html
                                     """))

    parser.add_argument("api_keys", nargs=2, help="Twitter API App key and secret")
    parser.add_argument("-u", "--users", nargs="?", help="Output file for user data")
    parser.add_argument("-t", "--tweets", nargs="?", help="Output file for tweet data")
    parser.add_argument("-l", "--limit", type=int,
                        help="Limit greater or equal 1 of tweets loaded for each user. Use -1 to get all available tweets. Default value is 200",
                        default=200)

    parser.add_argument("-f", "--file", nargs="?", help="Input file to be used")

    parser.add_argument("--usernames", action="store_true", help="The input file contains usernames instead user ids",
                        default=False)
    parser.add_argument("--csv", action="store_true", help="Store the file as csv file instead sqlite", default=False)
    parser.add_argument("--skip-header", action="store_true", help="Skip the first line of the input file",
                        default=False)

    args = parser.parse_args()

    if args.file is None:
        parser.error("ERROR: No input file.")

    if len(args.api_keys) != 2:
        parser.error("ERROR: Twitter API consumer key and secret are required")

    auth = tweepy.AppAuthHandler(args.api_keys[0], args.api_keys[1])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    users = load_csv_file(args.file, args.skip_header)

    if args.users is not None:
        print("Fetch users...")
        user_dataset_generator = UserDatasetGenerator(api)
        user_dataset_generator.get_users(users, filename=args.users, is_username=args.usernames, sqlite=not args.csv)

    if args.tweets is not None:
        print("Fetch tweets...")
        tweet_dataset_generator = TweetDatasetGenerator(api)
        tweet_dataset_generator.get_tweets_of_users(users, filename=args.tweets, limit=args.limit,
                                                    is_username=args.usernames, sqlite=not args.csv)


if __name__ == "__main__":
    main()
