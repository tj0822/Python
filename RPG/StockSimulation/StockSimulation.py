#-*- coding:utf-8 -*-

import datetime
import csv
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import numpy
import matplotlib.cm as cmx
import matplotlib.colors as colors
import pandas as pd

portfolio = list()

# 초기값 셋팅
stock = 0
seedmoney = 10000000
totalValue = 0
stock = 0


# buyUnit = 5
# balalce = seedmoney
investMoney = 0
profit = 0
stockValue = 0
totalProfitRate = 0

downLimitList = list()
profitRateList = list()
buyUnitList = list()
prl = list()

# 매매기준
upperRate = 0.1  # 수익률이 5%이상이면 매도
lowerRate = -0.1  # 손해율이 5%이상이면 매도


# 거래 횟수
buyCnt = 0  # 매도 횟수
sellCnt = 0  # 매수 횟수

# 전날종가 대비 떨어진 당일 시가 금액 비율 기준(1%이상 떨어졌으면 매수)
downLimit = -0.1

# 매매기준
upperRate = 0.1  # 수익률이 5%이상이면 매도
lowerRate = -0.1  # 손해율이 5%이상이면 매도

# 전날종가 대비 떨어진 당일 시가 금액 비율 기준(1%이상 떨어졌으면 매수)
downLimit = -0.001

# fileList = ['PRICE_001740(SK네트웍스).csv',
#             'PRICE_017670(SK텔레콤).csv',
#             'PRICE_023590(다우기술).csv'
#             'PRICE_034220(LG디스플레이).csv',
#             'PRICE_035420(Naver).csv',
#             'PRICE_035720(카카오).csv'
#             'PRICE_036570(엔씨소프트).csv',
#             'PRICE_066270(SK컴즈).csv',
#             'PRICE_181710(NHN엔터테인먼트)_encoding.csv']
def init():
    # 초기값 셋팅
    global stock
    stock = 0
    global totalValue
    totalValue = 0
    stock = 0
    global balalce
    balalce = seedmoney
    global investMoney
    investMoney = 0
    global profit
    profit = 0
    global stockValue
    stockValue = 0
    global totalProfitRate
    totalProfitRate = 0
    global buyCnt
    buyCnt = 0  # 매도 횟수
    global sellCnt
    sellCnt = 0  # 매수 횟수
    global maxProfit
    maxProfit = 0
    profitRateList.clear()


def buy(stockPrice):
    # print('매수')
    global stock
    global buyUnit
    stock += buyUnit

    global investMoney
    investMoney += (stockPrice * buyUnit)

    global balalce
    balalce -= (stockPrice * buyUnit)

    global buyCnt
    buyCnt += 1


def sell(stockPrice):
    # print('매도')
    global stock
    global balalce
    balalce += stockPrice * stock
    stock = 0

    global investMoney
    investMoney = 0

    global sellCnt
    sellCnt += 1


def buyOrSell():
    # 0 : hold, 1 : buy, 2 : sell
    if (profitRate > upperRate or profitRate < lowerRate):
        return 2
    else:
        if (balalce > todayStartPrice and rate < downLimit):
            return 1
        else:
            return 0


# fileList = ['PRICE_181710(NHN엔터테인먼트)_encoding.csv']

for fileName in fileList:
    print(fileName)

    stockData = open('data/' + fileName, 'r', encoding='euc-kr')
    reader = csv.reader(stockData)
    stockList = list(reader)

    # firstDate = datetime.datetime.strptime(stockList[1][0], "%Y.%m.%d").date()
    # lastDate = datetime.datetime.strptime(stockList[stockList.__len__()-1][0], "%Y.%m.%d").date()
    # firstDate = datetime.datetime.strptime(stockList[1][0], "%Y-%m-%d").date()
    firstDate = datetime.datetime.strptime('2016-01-01', "%Y-%m-%d").date()
    lastDate = datetime.datetime.strptime(stockList[stockList.__len__()-1][0], "%Y-%m-%d").date()

    if firstDate > lastDate:
        stockList.sort(reverse=False)
        tmpFirstDate = lastDate
        lastDate = firstDate
        firstDate = tmpFirstDate

    nMax = 1
    for n in range(1, nMax+1):

        buyUnit = n
        k = -2
        for d in range(-1, k, -1):
            downLimit = d / 100
            # legend = (n, downLimit)
            # cmap = get_cmap(11)
            init()
            # 시뮬레이션 투자 기간
            day_count = 30

            for i in range(0, day_count, 1):
                startDate = firstDate + datetime.timedelta(days=i)
                # endDate = startDate + relativedelta(years=1)
                endDate = startDate + relativedelta(months=1)

                for j in range(0, stockList.__len__() - 1):
                    if j < 2:
                        continue
                    else:
                        # today = datetime.datetime.strptime(stockList[j][0], "%Y.%m.%d").date()
                        today = datetime.datetime.strptime(stockList[j][0], "%Y-%m-%d").date()
                        # print(today)
                        # print(startDate)
                        # print(lastDate)
                        # print(endDate)
                        if (today >= startDate and (today <= lastDate and today <= endDate )):
                            # 전날 종가
                            prevFinalPrice = int(stockList[j-1][1])

                            # 오늘 시가
                            todayStartPrice = int(stockList[j][2])

                            # 현재 보유 주식 가치
                            stockValue = todayStartPrice * stock
                            # 손익 금액
                            profit = stockValue - investMoney
                            # 손익률
                            if investMoney > 0:
                                profitRate = profit / investMoney
                            else:
                                profitRate = 0
                            # 변동폭
                            diff = todayStartPrice - prevFinalPrice
                            # 변동률
                            rate = diff / prevFinalPrice

                            # print('전날 종가 : ', prevFinalPrice)
                            # print('오늘 시가 : ', todayStartPrice)
                            # print('보우 주식수 : ', stock)
                            # print('보유 주식 가치 : ', stockValue)
                            # print('손익 금액 : ', profit)
                            # print('투자 손익률 : ', profitRate)
                            # print('총 투자금액 : ', investMoney)
                            # print('현금 잔고 : ', balalce)
                            # print('총 자산 : ', balalce + stockValue)
                            # print('변동폭 : ', diff)
                            # print('변동률 : ', rate)
                            # print('총 손익률 : ', ((balalce + stockValue) / seedmoney) - 1)

                            if buyOrSell() == 2:
                                sell(todayStartPrice)
                            if buyOrSell() == 1:
                                buy(todayStartPrice)
                            if buyOrSell() == 0:
                                continue

                            # print("")

                totalProfitRate = (balalce + stockValue) / seedmoney - 1
                # print(totalProfitRate)
                profitRateList.append((totalProfitRate, downLimit, buyUnit, startDate))

                print(today, '부터', buyUnit, '주씩', downLimit, '기준으로 거래하면 수익률 : ', totalProfitRate)
                # plt.scatter(downLimit, len([x for x in profitRateList if x > 0]) / len(profitRateList), c=cmap(abs(n)))
            # print(pd.DataFrame(profitRateList))

            dfProfitRateList = pd.DataFrame(profitRateList)
            r = len(dfProfitRateList[dfProfitRateList[0] > 0]) / len(dfProfitRateList[0])
            prl.append((downLimit, n, r))

            print(day_count, '일 동안', downLimit, n, '주씩 매수하면', '수익 확률 : ', r)
            # plt.scatter(d, len([x for x in profitRateList if x > 0]) / len(profitRateList), c=cmap(abs(d)))

            # plt.plot(dateList, profitRateList, label=legend)
            # plt.plot(dateList, profitRateList, label=legend)
            # plt.legend(loc='upper right')


    # print(startDate, ':', max(tmpProfitRateList)[1], ':', max(tmpProfitRateList)[0], ':', max(tmpProfitRateList)[2])
    df = pd.DataFrame(prl)
    # print(df)

    outputFileName = fileName + '_output.csv'
    with open(outputFileName, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in prl:
            writer.writerow(row)
    csvfile.close()


# for n in range(1, nMax+1):
#     plt.scatter(df[0][df[1] == n], df[2][df[1] == n], c=cmap(abs(n)), label=n)
#
# plt.legend()
# plt.show()


# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# ax.plot(dateList, downLimitList, profitRateList, label='profit')
# plt.show()



# fig = plt.figure()
# ax = plt.subplot(3, 1, 1)

# ax = plt.subplot(3, 1, 2)
# plt.plot(dateList, downLimitList)
#
# ax = plt.subplot(3, 1, 3)
# plt.plot(dateList, buyUnitList)

# plt.show()


## scatter3d
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# ax.set_xlabel('Date')
# ax.set_ylabel('downLimit')
# ax.set_zlabel('profit')
#
# ax.scatter(dateList, downLimitList, profitRateList)
# plt.show()