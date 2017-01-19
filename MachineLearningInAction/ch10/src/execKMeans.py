'''
Created on 2016. 2. 9.

@author: TaijinKim
'''

import kMeans
from numpy import *

dataMat = mat(kMeans.loadDataSet('../data/testSet.txt'))
# print(min(dataMat[:, 0]))
# print(min(dataMat[:, 1]))
# print(max(dataMat[:, 1]))
# print(max(dataMat[:, 0]))
# 
print(kMeans.randCent(dataMat, 2))
# 
# print(kMeans.distEclud(dataMat[0], dataMat[1]))
# myCentroids, clustAssing = kMeans.kMeans(dataMat, 4)
