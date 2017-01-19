#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# 데이터 load
trainData = pd.read_csv("../data/train.csv")

# 리스트 원소간 거리구하기(두 점 사이 거리 구하기)
def calcDistance(trainList, testList):
    d = 0
    if len(trainList) == len(testList):
        size = len(trainList)

        for idx in range(0, size):
            d += (float(trainList[idx]) - float(testList[idx])) ** 2
        return math.sqrt(d)

    else:
        print('리스트의 크기가 다릅니다.')

# print(calcDistance(trainData[1:2].values.tolist()[0][1:94], trainData[2:3].values.tolist()[0][1:94]))

for i in range(0, len(trainData)):
    print(calcDistance(trainData[i:i+1].values.tolist()[0][1:94], trainData[i+1:i+2].values.tolist()[0][1:94]))