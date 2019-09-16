#-*- coding:utf-8 -*-
import random
import lotto_statistics as statistics
from numpy.random import choice

def GenByRandom(cnt=1):
    numList = []
    for i in range(1, cnt+1):
        numList.append(random.sample(list(range(1, 46)), 6))
    return numList

def GenByNumCnt(lottoHistory=None, series=None, cnt=None):
    lottoDictByNumber = statistics.GetLottoDicByNumber(lottoHistory[lottoHistory['series'] < series])

    return GetRecommenedNumbersByNumCnt(lottoDictByNumber)

def GetRecommenedNumbersByNumCnt(lottoDictByNumber):
    # 선택할 sum 숫자수
    pickSumCount = 5

    # 번호별 분포 확률
    pList = [x / sum(lottoDictByNumber.values()) for x in lottoDictByNumber.values()]

    # 추천 번호 리스트
    pickNumberList = []

    cnt = 0
    while (cnt < pickSumCount):
        pickNumber = choice(list(lottoDictByNumber.keys()), 6, p=pList)
        if len(set(pickNumber)) == 6:
            cnt += 1
            pickNumberList.append(sorted(list(pickNumber)))
        else:
            continue

    return pickNumberList

def GenBySum(lottoHistory=None, series=None, cnt=None):
    lottoDictBySum = statistics.GetLottoDicBySum(lottoHistory[lottoHistory['series'] < series])
    print(lottoDictBySum)

