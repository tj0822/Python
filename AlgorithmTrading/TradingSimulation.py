#-*- coding:utf-8 -*-

import pandas as pd
from os import listdir
from os.path import isfile, join
import datetime
import csv

stockDirectory = 'data/2017-11-04/'

outputFileName = 'output_2017-12-18_A3.csv'
result = pd.read_csv(outputFileName, dtype={'종목코드': str}).sort(['날짜', '거래유형'], ascending=[True, False])
result = result.reset_index(drop=True)
result['날짜'] = pd.to_datetime(result['날짜'], format="%Y-%m-%d")


maxSeedMoney = 50000000
baseMoney = 30000000
deposit = maxSeedMoney - baseMoney

totalSeedMoney = baseMoney
currentMoney = baseMoney

outComeUnit = 10000000

unitPrice = 1000000     #주식거래 단위 금액
currentValue = 0

portfolio = dict()
fromSimulDate = datetime.datetime.strptime(str(2010) + '-01-01', "%Y-%m-%d").date()
toSimulDate = datetime.datetime.strptime((str(2017) + '-01-01'), "%Y-%m-%d").date()

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

f = open(str(fromSimulDate)[:4] + '~' + str(toSimulDate)[:4] + '_' + str(datetime.datetime.now()).split('.')[0].replace('-', '').replace(':','').replace(' ', '') + '_' + outputFileName.replace('-', ''), 'w', newline='')
wr = csv.writer(f)
wr.writerow(['날짜', '거래유형', '종목코드', '거래가격', '거래수량', '주식가치', '현금자산', '총자산', '인'])

for i in range(0, result.__len__()):
    date = datetime.datetime.strptime(str(result['날짜'][i])[:10], "%Y-%m-%d").date()
    sellOrBuy = result['거래유형'][i]
    stockCode = result['종목코드'][i]
    stockName = result['종목명'][i]
    tradePrice = result['거래가격'][i]
    successCnt = result['성공'][i]
    failCnt = result['실패'][i]
    stockCount = 0

    if date >= fromSimulDate:
        if date > toSimulDate:
            break

        else:
            if sellOrBuy == 'buy' and successCnt > failCnt:
                # 매수
                if currentMoney < unitPrice and totalSeedMoney < maxSeedMoney:
                    currentMoney += unitPrice
                    totalSeedMoney += unitPrice
                    deposit -= unitPrice

                stockCount = int(min([unitPrice, currentMoney]) / tradePrice)

                if stockCount > 0:
                    portfolio[stockCode] = stockCount
                    inputMoney = stockCount * tradePrice
                    currentMoney -= inputMoney
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
                    currentMoney += outComeMoney
                    del portfolio[stockCode]

                # print('잔고 : ', seedMoney)
                # print(currentCashValue)
                # print(portfolio)

            stockValue = GetStockValue(portfolio, date)
            if currentMoney > outComeUnit and currentMoney + stockValue > baseMoney + outComeUnit:
                deposit += outComeUnit
                currentMoney -= outComeUnit
                totalSeedMoney -= outComeUnit

            totalValue = currentMoney + stockValue

            if stockCount > 0:
                print('날짜 :', str(date)[:10], '총 투자금액 :', totalSeedMoney, '유형 :', sellOrBuy, '종목 :', stockCode, '가격 :', tradePrice, '수량 :', stockCount, '주식 :', stockValue, '현금 :', currentMoney, '주식계좌 :', totalValue, '일반계좌 :', deposit)
                wr.writerow([str(date)[:10], totalSeedMoney, sellOrBuy, stockCode, tradePrice, stockCount, stockValue, currentMoney, totalValue, deposit])
    else:
        continue

f.close()
