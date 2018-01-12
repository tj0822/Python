#-*- coding:utf-8 -*-

import random
import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import RPG.MoneyBot.AibrilNLU as alu
import RPG.MoneyBot.Stock as Stock
import csv
import numpy as np

stockDirectory = 'data/2017-11-04/'
# stockFiles = (f for f in listdir(stockDirectory) if isfile(join(stockDirectory, f)))
kospiList= Stock.GetKospi200()

# 1. 종목 선정
class SelectStocks:
    def GetPortfolio(self):
        return {'035720', '000660', '066570'}

# 2. 일자별 의사결정: 매수/매도/Holding
class MakeDecision:
    # -1: sell 0:stay 1:buy
    def Decision(stockName, date):
        return alu.getScore(stockName, date)

# 3. 거래 : 날짜,거래유형,종목코드,거래가격,거래수량,주식가치,현금자산,총자산
class Trading:
    def Simulation(stock = None, seedMoney = 1000000, fromDate='2016-01-01', toDate='2016-12-31', algorithmNumber = 0):
        fromSimulDate = datetime.datetime.strptime(str(fromDate), "%Y-%m-%d").date()
        toSimulDate = datetime.datetime.strptime((str(toDate)), "%Y-%m-%d").date()
        cashValue = seedMoney
        stockCnt = 0
        # 가격데이터 가져오기(나중에 DB select로 변경 예정)
        stockPriceDF = pd.read_csv(stockDirectory + stock + '_' + kospiList[stock] + '.csv').sort_values(['datetime'])
        for i in range(0, len(stockPriceDF)):
            date = datetime.datetime.strptime(stockPriceDF[i:i + 1]['datetime'].values[0], "%Y-%m-%d").date()
            volume = int(stockPriceDF[i:i + 1]['volume'])
            if date >= fromSimulDate and (int(stockPriceDF[i - 1:i]['volume']) * volume) > 0 and date <= toSimulDate:
                descisionScore = MakeDecision.Decision(kospiList[stock], date)
                # open = int(stockPriceDF[i:i + 1]['open'])
                close = int(stockPriceDF[i:i + 1]['close'])
                # low = int(stockPriceDF[i:i + 1]['low'])
                # high = int(stockPriceDF[i:i + 1]['high'])

                tradeCnt = 0

                if descisionScore > 0 and stockCnt == 0:
                    stockCnt = int(cashValue / close)
                    tradeCnt = stockCnt
                elif descisionScore == 0:
                    tradeCnt = 0
                elif descisionScore < 0 and stockCnt > 0:
                    tradeCnt = stockCnt
                    stockCnt = 0

                cashValue -= close * tradeCnt * np.sign(descisionScore)
                stockValue = close * stockCnt

                # 4. 거래 이력 output
                wr.writerow([date, descisionScore, np.sign(descisionScore), stock, kospiList[stock], close, tradeCnt,stockValue, cashValue, (stockValue + cashValue)])
                print('날짜:', date,
                      'score:', descisionScore,
                      '거래유형:', np.sign(descisionScore),
                      '종목코드:', stock,
                      '종목명:', kospiList[stock],
                      '거래가격:', close,
                      '거래수량:', tradeCnt,
                      '주식가치:', stockValue,
                      '현금자산:', cashValue,
                      '총자산:', stockValue + cashValue)


# 4. 성과 분석
'''
input 파라미터 : 종목코드, 초기자본, 시뮬레이션 기간, 알고리즘 코드
'''

portfolio = SelectStocks.GetPortfolio(None)

f = open('../RPG/MoneyBot/output/' + str(datetime.datetime.now()) + '.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerow(['날짜', 'score', '거래유형', '종목코드', '종목명', '거래가격', '거래수량', '주식가치', '현금자산', '총자산'])

for stock in portfolio:
    Trading.Simulation(stock = stock,
                        seedMoney = 1000000,
                        fromDate = '2016-01-01',
                        toDate = '2017-12-31',
                        algorithmNumber = 0)

f.close()