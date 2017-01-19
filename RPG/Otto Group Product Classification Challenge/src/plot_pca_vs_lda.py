#-*- coding:utf-8 -*-

print(__doc__)

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

trainData = pd.read_csv("../data/train.csv")

X = np.asarray(trainData.loc[:,'feat_1':'feat_93'])
y = np.asarray(trainData.loc[:,'target'])
target_names = list(set())

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

# Percentage of variance explained for each components
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

print(target_names)
plt.figure()
for c, i, target_name in zip("rgb", list(range(0,len(trainData)-1)), target_names):
    print(i)
    print(c)
    plt.scatter(X_r[i][0], X_r[i][1], label=target_name)
plt.legend()
plt.title('PCA')

plt.figure()
for c, i, target_name in zip("rgb", range(0,len(trainData)-1), target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
plt.legend()
plt.title('LDA')

plt.show()