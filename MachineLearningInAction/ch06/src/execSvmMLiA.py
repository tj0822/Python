#-*- coding:utf-8 -*-
'''
Created on 2015. 10. 27.

@author: KimTaeJin
'''
import svmMLiA
from numpy import * 

# dataArr, labelArr = svmMLiA.loadDataSet('../data/testSet.txt')
# print(labelArr)


# reload(svmMLiA)
# b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
# 
# print(b)
# print(alphas[alphas>0])

# b, alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 40)
# 
# ws = svmMLiA.calcWs(alphas, dataArr, labelArr)
# print(ws)
# 
# dataMat = mat(dataArr)
# dataMat[0] * mat(ws) + b

# reload(svmMLiA)
# svmMLiA.testRbf()

# reload(svmMLiA)
svmMLiA.testDigits(('rbf', 20))