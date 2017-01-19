#-*- coding:utf-8 -*-
'''
Created on 2015. 10. 22.

@author: KimTaeJin
'''
import logRegres
from numpy import *

# dataArr, labelMat = logRegres.loadDataSet()
# logRegres.gradAscent(dataArr, labelMat)
# reload(logRegres)
# weights = logRegres.gradAscent(dataArr, labelMat)
# logRegres.plotBestFit(weights.getA()


# reload(logRegres)
# dataArr, labelMat = logRegres.loadDataSet()
# weights = logRegres.stocGradAscent0(array(dataArr), labelMat)
# logRegres.plotBestFit(weights)


# reload(logRegres)
# dataArr, labelMat = logRegres.loadDataSet()
# weights = logRegres.stocGradAscent1(array(dataArr), labelMat)
# logRegres.plotBestFit(weights)


reload(logRegres)
logRegres.multiTest()