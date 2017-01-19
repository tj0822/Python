# -*- coding: utf-8 -*-
'''
Created on 2015. 9. 4.

@author: TaijinKim
'''

#테스
from numpy import *
data = random.rand(4,4)
print(data)

randMat = mat(random.rand(4,4))
print(randMat)

invRandMat = randMat.I
print(invRandMat)

myEye = randMat * invRandMat
print(myEye)

print(myEye - eye(4))