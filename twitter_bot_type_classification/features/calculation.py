import os
from multiprocessing import Queue, Process, Lock

import numpy as np

from twitter_bot_type_classification.features.user import UserFeatures


class CalcWorker(Process):
    def __init__(self, task_q, results_q):
        self.task_q = task_q
        self.results_q = results_q
        super(CalcWorker, self).__init__()

    def run(self):
        while True:
            feature_data = self.task_q.get()
            if feature_data is None:
                self.results_q.put(None)
                break

            user, tweets = feature_data
            features = UserFeatures(user, tweets)

            self.results_q.put((user.id, features))


class SaveWorker(Process):
    def __init__(self, results_q, filename, fetch_worker_count, std_out_lock):
        self.results_q = results_q
        self.filename = filename
        self.fetch_worker_count = fetch_worker_count
        self.std_out_lock = std_out_lock
        super(SaveWorker, self).__init__()

    def run(self):
        features = []
        user_ids = []
        while True:
            res = self.results_q.get()
            if res is None:
                self.fetch_worker_count -= 1
                if self.fetch_worker_count == 0:
                    np.savez_compressed(self.filename, features=np.asarray(features), ids=np.asarray(user_ids))

                    self.std_out_lock.acquire()
                    print("\nSuccessfully saved features as npz file")
                    self.std_out_lock.release()

                    break
            else:
                user_ids.append(res[0])
                features.append(res[1])


class FeatureCalculator:
    save_worker = None

    def __init__(self, tasks_q_size=100, results_q_size=100):

        assert tasks_q_size > 0
        assert results_q_size > 0

        self.tasks_q_size = tasks_q_size
        self.results_q_size = results_q_size
        self.std_out_lock = Lock()

    def calc_features(self, user_db, tweet_db, filename, limit=500, n_worker=os.cpu_count()):
        assert user_db is not None and tweet_db is not None
        assert filename is not None
        assert limit > -2
        assert n_worker is not None and n_worker > 0

        tasks_q = Queue(self.tasks_q_size)
        results_q = Queue(self.results_q_size)
        workers = []

        for _ in range(n_worker):
            worker = CalcWorker(tasks_q, results_q)
            workers.append(worker)
            worker.start()

        for u in user_db.get_all_user():
            tweets = []
            if tweet_db is not None:
                tweets = tweet_db.get_tweets_for_user(u.id)
                tweets.sort(key=lambda t: t.id, reverse=True)

            tasks_q.put((u, tweets))

        for _ in range(len(workers)):
            tasks_q.put(None)

        self.save_worker = SaveWorker(results_q, filename, len(workers), self.std_out_lock)
        self.save_worker.start()

        self.save_worker.join()
