#-*- coding:utf-8 -*-
'''
Created on 2015. 11. 5.

@author: KimTaeJin
'''
import regression
from numpy import *

# xArr, yArr = regression.loadDataSet('../data/ex0.txt')
# 
# print(xArr[0:2])
# 
# ws = regression.standRegres(xArr, yArr)
# print(ws)
# 
# xMat = mat(xArr)
# yMat = mat(yArr)
# yHat = xMat * ws
# 
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
# 
# xCopy = xMat.copy()
# xCopy.sort(0)
# yHat = xCopy * ws
# print(yHat)
# # ax.plot(xCopy[:, 1], yHat)
# plt.show()

# xArr, yArr = regression.loadDataSet('../data/ex0.txt')
# print(yArr[0])
# print(regression.lwlr(xArr[0], xArr, yArr, 1.0))
# print(regression.lwlr(xArr[0], xArr, yArr, 0.001))
# 
# yHat = regression.lwlrTest(xArr, xArr, yArr, 0.003)
# xMat = mat(xArr)
# srtInd = xMat[:, 1].argsort(0)
# xSort = xMat[srtInd][:, 0, :]
# 
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # ax.plot(xSort[:, 1], yHat[srtInd])
# ax.scatter(xMat[:, 1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
# plt.show()


# abX, abY = regression.loadDataSet('../data/abalone.txt')
# ridgeWeights = regression.ridgeTest(abX, abY)
# print(ridgeWeights)
# 
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(ridgeWeights)
# plt.show()



xArr, yArr = regression.loadDataSet('../data/abalone.txt')
regression.stageWise(xArr, yArr, 0.01, 200)