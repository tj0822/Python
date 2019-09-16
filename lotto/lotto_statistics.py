#-*- coding:utf-8 -*-
import MySQL as sql
import matplotlib.pyplot as plt
import pandas as pd


'''
입력한 회차의 직전 당첨이력 조회
'''
def getLottoHistory(lastSeries):
    query = "SELECT series, n1, n2, n3, n4, n5, n6, bonus_n, total_winner, each_price from lotto_history where series < %d" %lastSeries
    result = sql.selectStmt(query)

    lottoList = []
    for row in result:
        lottoList.append(row)

    return lottoList

'''
입력한 특정 회차 조회
'''
def getLottoOneResult(series):
    query = "SELECT series, n1, n2, n3, n4, n5, n6, bonus_n, total_winner, each_price from lotto_history where series = %d" %series
    result = sql.selectStmt(query)

    lottoList = []
    for row in result:
        lottoList.append(row)

    return lottoList

'''
모든 결과 list select
'''
def getLottoAllResult():
    query = "SELECT series, n1, n2, n3, n4, n5, n6, bonus_n, total_winner, each_price from lotto_history"
    result = sql.selectStmt(query)

    lottoList = []
    for row in result:
        lottoList.append(row)

    lottoDf = pd.DataFrame(lottoList)
    lottoDf.columns = ['series', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'bonus_n', 'total_winner', 'each_price']
    lottoDf = lottoDf.sort_values(by='series')

    return lottoDf

# lotto번호 dictionary정의
def getLottoDic(lottoHistory):
    lottoDictByNumber = {}
    lottoDictBySum = {}

    #dictionary 정의
    for i in range(1, 46):
        lottoDictByNumber[i] = 1

    for i in range(sum(list(range(1, 7))), sum(list(range(40, 46)))+1):
        lottoDictBySum[i] = 1

    # print(lottoHistory)
    for row in lottoHistory.iterrows():

        print(row[1:7])
        # lottoDictBySum[list(pd.Series(row).values[0])[1:7]] += 1
        lottoDictBySum[row[1:7]] += 1

        for i in range(0, 7):
            lottoDictByNumber[list(row.values[0])[i]] += 1

    return lottoDictByNumber, lottoDictBySum

'''
번호별 당첨 count
'''
def GetLottoDicByNumber(lottoHistory):
    lottoDictByNumber = {}

    #dictionary 정의
    for i in range(1, 46):
        lottoDictByNumber[i] = 1

    for row in lottoHistory.iterrows():
        for i in range(1, 8):
            lottoDictByNumber[row[1][i]] += 1

    return lottoDictByNumber

'''
총 합별 당첨 횟수 count
'''
def GetLottoDicBySum(lottoHistory):
    lottoDictBySum = {}

    for i in range(sum(list(range(1, 7))), sum(list(range(40, 46)))+1):
        lottoDictBySum[i] = 1

    # print(lottoHistory)
    for row in lottoHistory.iterrows():
        lottoDictBySum[list(pd.Series(row).values[0])[1:7]] += 1

    return lottoDictBySum

# 회차별 당첨번호 sum count하기
def getSumCountDict(sum, sumDict):
    if sum in sumDict.keys():
        sumDict[sum] += 1
    else:
        sumDict[sum] = 1

    return sumDict


# result = getLottoAllResult()
# print(result)
