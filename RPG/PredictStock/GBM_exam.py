#-*- coding:utf-8 -*-

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import make_hastie_10_2
import matplotlib.pyplot as plt

X, y = make_hastie_10_2(n_samples=10000)

est = GradientBoostingClassifier(n_estimators=2000, max_depth=1).fit(X, y)


# get predictions
# pred = est.predict(X)
# print(est.predict_proba(X)[0])

plt.figure()
for pred in est.staged_predict(X):
    plt.plot(X[:, 0], pred, color='r', alpha=0.1)

plt.show()