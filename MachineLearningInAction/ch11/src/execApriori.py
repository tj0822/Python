#-*- coding:utf-8 -*-

import MachineLearningInAction.ch11.src.apriori as apriori

dataSet = apriori.loadDataSet()
print(dataSet)
C1 = apriori.createC1(dataSet)
print(C1)
D = map(set, dataSet)
print(D)