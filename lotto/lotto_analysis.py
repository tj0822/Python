#-*- coding:utf-8 -*-


import lotto.MySQL as sql
from numpy.random import choice


# lotto번호 dictionary정의
def getLottoDic(lottoHistory):
    lottoDictByNumber = {}
    sumDict = {}
    for i in range(1, 46):
        lottoDictByNumber[i] = 0

    for row in lottoHistory:
        lottoDictBySum = getSumCountDict(sum(row[1:7]), sumDict)

        for i in range(1, 8):
            lottoDictByNumber[int(row[i])] += 1

    return lottoDictByNumber, lottoDictBySum

# lotto당첨 이력 가져오기
def getLottoHistory():
    query = "SELECT series, n1, n2, n3, n4, n5, n6, bonus_n, total_winner, each_price from lotto_history"
    result = sql.selectStmt(query)

    lottoList = []
    for row in result:
        lottoList.append(row)

    return lottoList

# 회차별 당첨번호 sum count하기
def getSumCountDict(sum, sumDict):
    if sum in sumDict.keys():
        sumDict[sum] += 1
    else:
        sumDict[sum] = 1

    return sumDict


# 번호 추천
def getLottoNum(lottoDictBySum, lottoDictByNumber):
    # 선택할 sum 숫자수
    pickSumCount = 5
    pSumList = [x / sum(lottoDictBySum.values()) for x in lottoDictBySum.values()]

    # 확률 가중치에 의해 랜덤으로 pickSumCount만큼 추출
    pickSumList = choice(list(lottoDictBySum.keys()), pickSumCount, p=pSumList)

    # 번호별 분포 확률
    pList = [x / sum(lottoDictByNumber.values()) for x in lottoDictByNumber.values()]

    # 추천 번호 리스트
    pickNumberList = []

    cnt = 0
    for i in sorted(pickSumList):
        while(cnt < pickSumCount):
            pickNumber = choice(list(lottoDictByNumber.keys()), 6, p=pList)

            if len(set(pickNumber)) == 6:
                if i == sum(pickNumber):
                    cnt += 1
                    pickNumberList.append(list(pickNumber))
                    break
                else:
                    continue

    return pickNumberList



# lotto history 가져오기
def getRecommendNumbers():
    lottoHistory = getLottoHistory()

    lottoDictByNumber, lottoDictBySum = getLottoDic(lottoHistory)

    pickNumberList = getLottoNum(lottoDictBySum, lottoDictByNumber)

    for row in pickNumberList:
        print(row)

    return str(pickNumberList)

