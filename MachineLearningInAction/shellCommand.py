#-*- coding:utf-8 -*-
'''
Created on 2015. 10. 25.

@author: KimTaeJin
'''

from numpy import *
dataMat = []
dataMat.append((1,1))
dataMat.append((2,2))
dataMat.append((3,3))
dataMat.append((5,3))

m, n = shape(dataMat)   # m행 n열인지 알기
print(m, n) 