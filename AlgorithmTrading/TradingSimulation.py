#-*- coding:utf-8 -*-

import pandas as pd
from os import listdir
from os.path import isfile, join
import datetime
import csv

stockDirectory = 'data/2017-11-04/'

outputFileName = 'output_2017-12-10_A3.csv'
result = pd.read_csv(outputFileName, dtype={'종목코드': str}).sort(['날짜'])
result = result.reset_index(drop=True)
result['날짜'] = pd.to_datetime(result['날짜'], format="%Y-%m-%d")

seedMoney = 30000000


unitPrice = 1000000     #주식거래 단위 금액
currentValue = 0

portfolio = dict()
fromSimulDate = datetime.datetime.strptime(str(2015) + '-01-01', "%Y-%m-%d").date()
toSimulDate = datetime.datetime.strptime((str(2016) + '-01-01'), "%Y-%m-%d").date()

# result[result[datetime.datetime.strptime(result['날짜'], "%Y-%m-%d").date()] <= toSimulDate]
lastTradeDate = max(result['날짜'])

def GetStockValue(portfolio, date):
    currentStockValue = 0
    for key, value in portfolio.items():
        stockFiles = (f for f in listdir(stockDirectory) if isfile(join(stockDirectory, f)))
        for fileName in stockFiles:
            if fileName.split('_')[0] == key:
                portfolioStock = pd.read_csv(stockDirectory + fileName)
                portfolioStock['datetime'] = pd.to_datetime(portfolioStock['datetime'], format="%Y-%m-%d")
                # 가끔 거래 정지등으로 해당일자에 실적이 없을때 가장 최근 가격으로 사용함
                currentStockValue += int(portfolioStock[portfolioStock['datetime'] == max(portfolioStock[portfolioStock['datetime'] <= date]['datetime'])]['close']) * value

    # print(date, ' 주식 총 가치 : ',  currentStockValue)
    return currentStockValue

f = open('simulation_' + outputFileName, 'w', newline='')
wr = csv.writer(f)
wr.writerow(['날짜', '거래유형', '종목코드', '거래가격', '거래수량', '주식가치', '현금자산', '총자산'])

for i in range(0, result.__len__()):
    date = result['날짜'][i]
    sellOrBuy = result['거래유형'][i]
    stockCode = result['종목코드'][i]
    stockName = result['종목명'][i]
    tradePrice = result['거래가격'][i]

    if sellOrBuy == 'buy':
        # 매수
        stockCount = int(min([unitPrice, seedMoney]) / tradePrice)
        if stockCount > 0:
            portfolio[stockCode] = stockCount
            inputMoney = stockCount * tradePrice
            seedMoney -= inputMoney
        else :
            continue
        # print('잔고 : ', seedMoney)
        # print(currentCashValue)
        # print(portfolio)
    elif sellOrBuy == 'sell':
        # 매도
        if portfolio.__contains__(stockCode):
            stockCount = portfolio[stockCode]
            outComeMoney = stockCount * tradePrice
            seedMoney += outComeMoney
            del portfolio[stockCode]

        # print('잔고 : ', seedMoney)
        # print(currentCashValue)
        # print(portfolio)

    stockValue = GetStockValue(portfolio, date)
    totalValue = seedMoney + stockValue
    print('날짜 : ', str(date)[:10], '거래유형 : ', sellOrBuy, ' 종목코드 : ', stockCode, ' 거래가격 : ', tradePrice, ' 거래수량 : ', stockCount, ' 주식가치 : ', stockValue, ' 현금자산 : ', seedMoney, ' 총자산 : ', totalValue)

    wr.writerow([str(date)[:10], sellOrBuy, stockCode, tradePrice, stockCount, stockValue, seedMoney, totalValue])


f.close()
