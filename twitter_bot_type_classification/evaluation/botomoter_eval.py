import sys

import botometer

sys.path.append(".")

import tokens

twitter_app_auth = {
    "consumer_key": tokens.APP_KEY,
    "consumer_secret": tokens.APP_SECRET,
    "access_token": tokens.OAUTH_KEY,
    "access_token_secret": tokens.OAUTH_SECRET
}
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=tokens.RAPIDAPI_KEY,
                          **twitter_app_auth)

"""
dataset = np.load("../datasets/features/twitter_bot_dataset_eval.npz", allow_pickle=True)
X_train = dataset["X_train"]
X_test = dataset["X_test"]

y_train = dataset["y_train"]
y_test = dataset["y_test"]

ids_train = dataset["ids_train"]
ids_test = dataset["ids_test"]
"""

import csv

fetched_ids = set()

with open("../datasets/botometer_clf.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for r in reader:
        fetched_ids.add(int(r[0]))

print(len(fetched_ids))
exit()

error_ids = set()

with open("../datasets/eval_users_error.csv", "r") as f2:
    reader = csv.reader(f2)

    for r in reader:
        error_ids.add(int(r[0]))

ids = set()

with open("../datasets/eval_users_0.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for r in reader:
        user_id = int(r[0])
        if user_id not in fetched_ids and user_id not in error_ids:
            ids.add(user_id)

with open("../datasets/botometer_clf.csv", "a") as f:
    writer = csv.writer(f)

    with open("../datasets/eval_users_error.csv", "a") as f2:
        writer_error = csv.writer(f2)

        i = 0
        for screen_name, result in bom.check_accounts_in(ids):
            if "error" in result:
                writer_error.writerow([screen_name])
                continue

            print(i)
            writer.writerow([
                result["user"]["id_str"],
                result["scores"]["english"],
                result["scores"]["universal"],
                result["categories"]["content"],
                result["categories"]["friend"],
                result["categories"]["network"],
                result["categories"]["sentiment"],
                result["categories"]["temporal"],
                result["categories"]["user"],
                result["cap"]["english"],
                result["cap"]["universal"],
            ])

            i += 1
