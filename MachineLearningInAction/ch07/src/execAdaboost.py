#-*- coding:utf-8 -*-
'''
Created on 2015. 11. 3.

@author: KimTaeJin
'''

import adaboost
from numpy import *

# datMat, classLabels = adaboost.loadSimpData()

# D = mat(ones((5, 1))/5)
# adaboost.buildStump(datMat, classLabels, D)


# classifierArray = adaboost.adaBoostTrainDS(datMat, classLabels, 9)
# print(classifierArray)


# classifierArr = adaboost.adaBoostTrainDS(datMat, classLabels, 30)

# adaboost.adaClassify([0, 0], classifierArr)
# adaboost.adaClassify([[5, 5], [0, 0]], classifierArr)


# datArr, labelArr = adaboost.loadDataSet('../data/horseColicTraining2.txt')
# classifierArray = adaboost.adaBoostTrainDS(datArr, labelArr, 10)
# print(classifierArray)
# 
# testArr, testLabelArr = adaboost.loadDataSet('../data/horseColicTest2.txt')
# prediction10 = adaboost.adaClassify(testArr, classifierArray)
# print(prediction10)
# 
# errArr = mat(ones((67,1)))
# print(errArr[prediction10 != mat(testLabelArr).T].sum())


datArr, labelArr = adaboost.loadDataSet('../data/horseColicTraining2.txt')
classifierArray, aggClassEst = adaboost.adaBoostTrainDS(datArr, labelArr, 10)
adaboost.plotROC(aggClassEst.T, labelArr)