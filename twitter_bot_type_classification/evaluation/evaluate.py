import os
import time
from itertools import product
from multiprocessing import Process, Queue

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from mlxtend.plotting import plot_confusion_matrix
from sklearn.base import clone
from sklearn.metrics import f1_score, auc, roc_curve, confusion_matrix, log_loss, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import OneHotEncoder


def evaluate_model(basic_pipeline, X_data, y_data, labels, n_folds=5, random_state=42,
                   verbose=False, calc_log_loss=False):
    scores = {"f1_scores": [], "roc_auc_macro": [], "confusion_matrices": [], "bot_aucs": [], "bot_type_aucs": [],
              "class_scores": {}, "fpr_macro": [], "tpr_macro": []}
    for l in labels:
        scores["class_scores"][l] = {
            "f1_scores": [],
            "roc_aucs": [],
            "fpr": [],
            "tpr": []
        }

    if calc_log_loss:
        scores["log_loss"] = []

    start_time = time.time()

    params = basic_pipeline.get_params()

    for fold, (train_index, test_index) in enumerate(
            StratifiedKFold(n_splits=5, shuffle=True, random_state=random_state).split(X_data, y_data)):
        if verbose:
            print("calculating K-Fold {}/{}".format(fold + 1, n_folds))

        fold_start_time = time.time()

        pipeline = clone(basic_pipeline)
        pipeline.set_params(**params)

        X_train, X_test = X_data[train_index], X_data[test_index]
        y_train, y_test = y_data[train_index], y_data[test_index]

        pipeline.fit(X_train, y_train)

        y_pred_prob = pipeline.predict_proba(X_test)

        y_true = OneHotEncoder().fit_transform(y_test.reshape(-1, 1)).toarray()

        fpr = dict()
        tpr = dict()
        roc_aucs = dict()
        for i, l in enumerate(labels):
            fpr[l], tpr[l], _ = roc_curve(y_true[:, i], y_pred_prob[:, i])
            roc_aucs[l] = auc(fpr[l], tpr[l])

        all_fpr = np.unique(np.concatenate([fpr[l] for l in labels]))

        mean_tpr = np.zeros_like(all_fpr)
        for l in labels:
            mean_tpr += np.interp(all_fpr, fpr[l], tpr[l])

        mean_tpr /= len(labels)

        scores["fpr_macro"] = all_fpr
        scores["tpr_macro"] = mean_tpr

        y_pred = np.argmax(y_pred_prob, axis=1)

        f1_scores = f1_score(y_test, y_pred, average=None)

        mean_fpr = np.linspace(0, 1, 10)

        for i, l in enumerate(labels):
            scores["class_scores"][l]["f1_scores"].append(f1_scores[i])
            scores["class_scores"][l]["roc_aucs"].append(roc_aucs[l])

            scores["class_scores"][l]["fpr"].append(fpr[l])
            scores["class_scores"][l]["tpr"].append(tpr[l])

        scores["f1_scores"].append(np.mean(f1_scores))
        scores["roc_auc_macro"].append(auc(all_fpr, mean_tpr))
        scores["confusion_matrices"].append(confusion_matrix(y_test, y_pred))

        if calc_log_loss:
            scores["log_loss"].append(log_loss(y_test, y_pred_prob, eps=1e-15))

        y_test_2 = np.copy(y_test)
        y_test_2[y_test_2 != labels.index("human")] = -1

        # column 0: bot
        # column 1: human
        y_test_2_oh = OneHotEncoder().fit_transform(y_test_2.reshape(-1, 1)).toarray()

        y_pred_prob_2 = np.zeros((y_pred_prob.shape[0], 2))

        y_pred_prob_2[:, 1] = y_pred_prob[:, labels.index("human")]

        y_pred_prob_2[:, 0] = y_pred_prob[:, [i for i, n in enumerate(labels) if n != "human"]].sum(axis=1)

        scores["bot_aucs"].append(roc_auc_score(y_test_2_oh, y_pred_prob_2))

        y_test_2 = np.copy(y_test)
        # good bots
        y_test_2[y_test_2 == labels.index("content")] = -2
        y_test_2[y_test_2 == labels.index("feed")] = -2
        y_test_2[y_test_2 == labels.index("game")] = -2
        y_test_2[y_test_2 == labels.index("service")] = -2
        # bad bots
        y_test_2[y_test_2 == labels.index("fake_follower")] = -1
        y_test_2[y_test_2 == labels.index("political")] = -1
        y_test_2[y_test_2 == labels.index("social_spam")] = -1
        y_test_2[y_test_2 == labels.index("stock")] = -1
        y_test_2[y_test_2 == labels.index("traditional_spam")] = -1

        # column 0: good bot
        # column 1: bad bot
        # column 2: human
        y_test_2_oh = OneHotEncoder().fit_transform(y_test_2.reshape(-1, 1)).toarray()

        y_pred_prob_2 = np.zeros((y_pred_prob.shape[0], 3))
        # good bots
        y_pred_prob_2[:, 0] = y_pred_prob[:,
                              [i for i, n in enumerate(labels) if n in ["content", "feed", "game", "service"]]].sum(
            axis=1)
        # bad bots
        y_pred_prob_2[:, 1] = y_pred_prob[:, [i for i, n in enumerate(labels) if
                                              n in ["fake_follower", "political", "social_spam", "stock",
                                                    "traditional_spam"]]].sum(axis=1)

        y_pred_prob_2[:, 2] = y_pred_prob[:, labels.index("human")]

        scores["bot_type_aucs"].append(roc_auc_score(y_test_2_oh, y_pred_prob_2, average="macro", multi_class="ovr"))

        if verbose:
            print("{} Fold time: {:.2f}s".format(fold + 1, time.time() - fold_start_time))

    if verbose:
        print("\nTotal time: {:.2f}s".format(time.time() - start_time))
        print("\nFinished K-Fold evaluation")

    return scores


def print_eval(scores, labels, console_confm_print=True, confm_normed=True):
    print("F1 Score (macro): {:.3f}".format(np.mean(scores["f1_scores"])))
    print("ROC AUC (macro): {:.3f}".format(np.mean(scores["roc_auc_macro"])))
    print("Human Bot AUC: {:.3f}".format(np.mean(scores["bot_aucs"])))
    print("Bot type AUC (macro): {:.3f}".format(np.mean(scores["bot_type_aucs"])))

    if "log_loss" in scores:
        print("LOG LOSS (mean): {:.3f}".format(np.mean(scores["log_loss"])))

    for l in scores["class_scores"].keys():
        print(l)
        print("\tF1 Score (mean): {:.3f}".format(np.mean(scores["class_scores"][l]["f1_scores"], axis=0)))
        print("\tROC AUC (mean): {:.3f}".format(np.mean(scores["class_scores"][l]["roc_aucs"], axis=0)))

    total_confm = None

    for confm in scores["confusion_matrices"]:

        if total_confm is None:
            total_confm = confm
        else:
            total_confm = np.add(total_confm, confm)

    if console_confm_print:
        print()
        if confm_normed:
            print(np.true_divide(total_confm, total_confm.sum(axis=1, keepdims=True)).round(2))
        else:
            print(total_confm)
        print()
    else:
        fig, ax = plot_confusion_matrix(conf_mat=total_confm,
                                        colorbar=True,
                                        show_normed=confm_normed,
                                        class_names=labels,
                                        figsize=(10, 10))
        plt.show()


#     plt.figure()

#     plt.plot(scores["fpr_macro"], scores["tpr_macro"],
#         label="Macro ROC Kurve (Fläche = {0:0.2f})".format(np.mean(scores["roc_auc_macro"])),
#          color="navy", linestyle=":", linewidth=4)

#     for l in labels:
#         cl_scores = scores["class_scores"][l]
#         plt.plot(np.mean(cl_scores["fpr"], axis=0), np.mean(cl_scores["tpr"], axis=0), lw=2, label="ROC Kurve {0} (Fläche = {1:0.2f})".format(l, np.mean(cl_scores["roc_aucs"], axis=0)))

#     plt.plot([0, 1], [0, 1], 'k--', lw=2)
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.05])
#     plt.xlabel("False Positive Rate")
#     plt.ylabel("True Positive Rate")
#     plt.title("ROC Kurven unterschiedlicher Klassen und Macro Kurve")
#     plt.legend(loc="lower right")
#     plt.show()


class GridSearchWorker(Process):

    def __init__(self, grid_search_data_q, results_q, worker_times_q):
        self.grid_search_data_q = grid_search_data_q
        self.results_q = results_q
        self.worker_times_q = worker_times_q
        super(GridSearchWorker, self).__init__()

    def run(self):
        while True:
            grid_search_data = self.grid_search_data_q.get()
            if grid_search_data is None:
                self.results_q.put(None)
                break

            base_estimator, X, y, labels, n_fold, params = grid_search_data

            estimator = clone(base_estimator)
            estimator.set_params(**params)

            start_time = time.time()

            scores = evaluate_model(estimator, X, y, labels, verbose=False, n_folds=n_fold)

            self.worker_times_q.put(time.time() - start_time)

            self.results_q.put((params, scores))


class GridSearchWatch(Process):

    def __init__(self, worker_times_q, n_workers, n_jobs):
        self.worker_times_q = worker_times_q
        self.n_workers = n_workers
        self.n_jobs = n_jobs
        super(GridSearchWatch, self).__init__()

    def run(self):
        ended_worker = 0
        worker_times = []
        total_time = 0
        finished_jobs = 0
        avg_time = 0
        start_time = time.time()

        while True:
            if ended_worker == self.n_workers - 1:
                print("\nGrid search finished")
                break
            worker_time = self.worker_times_q.get()
            if worker_time is None:
                ended_worker += 1
            else:
                worker_times.append(worker_time)
                total_time += worker_time
                avg_time = avg_time * finished_jobs + worker_time
                finished_jobs += 1
                avg_time /= finished_jobs

                eta_time = (self.n_jobs - finished_jobs) / self.n_workers * avg_time / 60

                print("\r{}/{} (avg {:.2f}s/job, total: {:.1f}min, ETA: {:.1f}min)"
                    .format(
                    finished_jobs,
                    self.n_jobs,
                    avg_time,
                    (time.time() - start_time) / 60,
                    eta_time),
                    end="", flush=True)


class CustomGridSearchCV():
    def __init__(self, estimator, params, n_fold=5):
        if params is None:
            params = {}
        assert estimator is not None

        self.estimator = estimator
        self.params = params
        self.n_fold = n_fold

    def fit(self, X, y, labels):
        params_list = [dict(zip(self.params, v)) for v in product(*self.params.values())]

        print("Number of fits: {}".format(len(params_list)))

        grid_search_scores = {"params": [], "f1_scores": [], "fold_scores": []}

        grid_search_data_q = Queue(500)
        results_q = Queue()

        procs = []

        n_jobs = os.cpu_count()
        if len(params_list) < n_jobs:
            n_jobs = len(params_list)

        worker_times_q = Queue()

        watcher = GridSearchWatch(worker_times_q, n_jobs, len(params_list))
        watcher.start()

        for _ in range(n_jobs):
            p = GridSearchWorker(grid_search_data_q, results_q, worker_times_q)
            procs.append(p)
            p.start()

        for p in params_list:
            grid_search_data_q.put((self.estimator, X, y, labels, self.n_fold, p))

        for _ in range(len(procs)):
            grid_search_data_q.put(None)

        n_workers_finished = 0

        while True:
            result = results_q.get()
            if result is None:
                if n_workers_finished == len(procs) - 1:
                    break
                else:
                    n_workers_finished += 1
            else:
                grid_search_scores["params"].append((result[0]))
                grid_search_scores["f1_scores"].append(np.mean(result[1]["f1_scores"]))
                grid_search_scores["fold_scores"].append(result[1])

        #         for p in range(procs):
        #             p.join()

        #         watcher.join()

        return grid_search_scores


def plot_diff_train_size_f1(pipeline, X, y, model_name):
    train_sizes = []
    train_scores_mean = []
    test_scores_mean = []

    train_size_factors = np.linspace(0.1, 0.9, 9)

    params = pipeline.get_params()

    for size in train_size_factors:

        train_sizes.append(int(X.shape[0] * size))

        test_scores_fold = []
        train_scores_fold = []

        for train_index, test_index in StratifiedShuffleSplit(n_splits=5, train_size=size, random_state=42).split(X, y):
            f1_scores = []

            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

            pipeline = clone(pipeline)
            pipeline.set_params(**params)

            pipeline.fit(X_train, y_train)

            y_pred = pipeline.predict(X_test)
            test_scores_fold.append(np.mean(f1_score(y_test, y_pred, average=None)))

            y_pred = pipeline.predict(X_train)
            train_scores_fold.append(np.mean(f1_score(y_train, y_pred, average=None)))

        test_scores_mean.append(np.mean(test_scores_fold))
        train_scores_mean.append(np.mean(train_scores_fold))

    fig = go.Figure(data=[
        go.Scatter(x=train_size_factors, y=train_scores_mean, name="Train F1 Score"),
        go.Scatter(x=train_size_factors, y=test_scores_mean, name="Test F1 Score"),
    ])
    fig.update_layout(
        title="F1 Score Training und Test von " + model_name + " mit unterschiedlicher Trainingsdatengröße",
        xaxis_title="Faktor Anzahl Trainingsdaten",
        yaxis_title="5 Fold CV F1 Score")
    fig.show()
