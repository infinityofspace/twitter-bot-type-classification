import csv
import fcntl
import glob
import time
from itertools import repeat
from multiprocessing import Pool
from pathlib import Path

import tokens
import tweepy

DATASET_PATH = Path("../datasets/twitter_bot_dataset")


def get_users(api, ids, filename):
    all_ids = set(ids)

    users = api.lookup_users(ids, include_entities=False)

    timestamp = time.time()

    f = open(filename, "a")
    fcntl.flock(f, fcntl.LOCK_EX)

    writer = csv.writer(f)

    if f.tell() == 0:
        writer.writerow(["id", "active", "check_date"])

    for user in users:
        all_ids.remove(user.id)
        writer.writerow([user.id, 1, timestamp])

    for user_id in all_ids:
        writer.writerow([user_id, 0, timestamp])

    fcntl.flock(f, fcntl.LOCK_UN)
    f.close()


if __name__ == "__main__":

    auth = tweepy.OAuthHandler(tokens.APP_KEY, tokens.APP_SECRET)
    auth.set_access_token(tokens.OAUTH_KEY, tokens.OAUTH_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    pool = Pool()

    users_files = glob.glob(str(DATASET_PATH.joinpath("*/users.csv")))

    for user_file in users_files:
        print(user_file)
        user_ids = []
        with open(user_file, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                user_ids.append(int(r[0]))

        n_chunks = 100

        user_ids_chunks = [user_ids[i:i + n_chunks] for i in range(0, len(user_ids), n_chunks)]
        active_users_filename = user_file.replace("users.csv", "active_users.csv")
        pool.starmap(get_users, zip(repeat(api), user_ids_chunks, repeat(active_users_filename)))
