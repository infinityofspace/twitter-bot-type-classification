import argparse
import os
import textwrap

from twitter_bot_type_classification.dataset.db import CsvTweetDB, CsvUserDB, SqliteTweetDB, SqliteUserDB
from twitter_bot_type_classification.features.calculation import FeatureCalculator


def main():
    parser = argparse.ArgumentParser(description="Calculate tweet and user features from database.",
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

    parser.add_argument("-u", "--users", help="Input file of user data", required=True)
    parser.add_argument("-t", "--tweets", help="Input file of tweet data", required=True)
    parser.add_argument("-l", "--limit", type=int,
                        help="Limit of tweets to use for each user. If -1 all available tweets are used. Default value is -1",
                        default=-1)

    parser.add_argument("-f", "--file", help="Output fle to save the calculated features", required=True)

    parser.add_argument("-w", "--worker", type=int, help="Number of worker to use for the feature calculation",
                        required=False, default=os.cpu_count())
    parser.add_argument("--csv", action="store_true",
                        help="The provided input files are csv files. Default is sqlite database", default=False)
    parser.add_argument("--skip-header", action="store_true", help="Skip the first line of the csv input file",
                        default=False)

    args = parser.parse_args()

    if args.csv is None and args.skip_header:
        parser.error("ERROR: Can't skip the first line of a sqlite database.")

    if not args.users and not args.tweets:
        parser.error("ERROR: No user or tweets file provided.")

    if args.limit < -1:
        parser.error("ERROR: The tweet limit is not valid. Have to be greater or equal -1.")

    # Currently user and tweet db have to be provided.
    # On the task list is the independent calculation of the tweet and user features.
    if args.csv:
        tweet_db = None if args.tweets is None else CsvTweetDB(args.tweets, skip_header=args.skip_header)
        user_db = None if args.users is None else CsvUserDB(args.users, skip_header=args.skip_header)
    else:
        tweet_db = None if args.tweets is None else SqliteTweetDB(args.tweets)
        user_db = None if args.users is None else SqliteUserDB(args.users)

    feature_calculator = FeatureCalculator()

    feature_calculator.calc_features(user_db, tweet_db, args.file, limit=args.limit, n_worker=args.worker)


if __name__ == "__main__":
    main()
