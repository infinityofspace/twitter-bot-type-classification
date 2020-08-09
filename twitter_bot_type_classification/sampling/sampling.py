import os

from imblearn.over_sampling import ADASYN, SMOTE


def oversampling_adasyn(X, y, args):
    n_neighbors = args["n_neighbors"]
    sampling_strategy = args.get("sampling_strategy", None)
    random_state = args.get("random_state", 42)

    oversampling = ADASYN(sampling_strategy=sampling_strategy, n_neighbors=n_neighbors, random_state=random_state,
                          n_jobs=os.cpu_count())

    X_res, y_res = oversampling.fit_resample(X, y)

    return X_res, y_res


def oversampling_smote(X, y, args):
    sampling_strategy = args["sampling_strategy"]
    k_neighbors = args["k_neighbors"]
    random_state = args.get("random_state", 42)

    oversampling = SMOTE(sampling_strategy=sampling_strategy, k_neighbors=k_neighbors, random_state=random_state,
                         n_jobs=os.cpu_count())

    X_res, y_res = oversampling.fit_resample(X, y)

    return X_res, y_res
