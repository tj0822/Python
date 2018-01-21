#-*- coding:utf-8 -*-

import pandas as pd
import datetime

import RPG.MoneyBot.Stock as Stock
import csv
import RPG.MoneyBot.SelctStocks as portfolio
import RPG.MoneyBot.MakeDecision as decision
import RPG.MoneyBot.MySQL as sql


kospiList= Stock.GetKospi200()

# 1. 종목 선정
portfolios = portfolio.getPortfolio(None)

#

# 3. 거래 : 날짜,거래유형,종목코드,거래가격,거래수량,주식가치,현금자산,총자산
class Trading:
    def Simulation(stock = None, seedMoney = 1000000, fromDate='2016-01-01', toDate='2016-12-31', algorithmNumber = 0):
        fromSimulDate = datetime.datetime.strptime(str(fromDate), "%Y-%m-%d").date()
        toSimulDate = datetime.datetime.strptime((str(toDate)), "%Y-%m-%d").date()
        cashValue = seedMoney
        stockCnt = 0
        # 가격데이터 가져오기(나중에 DB select로 변경 예정)
        # stockPriceDF = pd.read_csv(stockDirectory + stock + '_' + kospiList[stock] + '.csv').sort_values(['datetime'])
        query = "SELECT CODE, DATE, PRICE_START, PRICE_HIGH, PRICE_LOW, PRICE_END, TRADE_AMOUNT FROM stock_price WHERE CODE = '%s' ORDER BY DATE" % stock
        rtn = sql.selectStmt(query)
        stockPriceDF = pd.DataFrame(rtn)
        stockPriceDF.columns = ['stockcode', 'datetime', 'close', 'high', 'low', 'open', 'volume']

        for i in range(0, len(stockPriceDF)):
            # date = datetime.datetime.strptime(stockPriceDF[i:i + 1]['datetime'].values[0], "%Y-%m-%d").date()
            date = stockPriceDF[i:i + 1]['datetime'].values[0]
            volume = int(stockPriceDF[i:i + 1]['volume'])
            if date >= fromSimulDate and (int(stockPriceDF[i - 1:i]['volume']) * volume) > 0 and date <= toSimulDate:
                # 2. 일자별 의사결정: 매수/매도/Holding
                descisionCode, tradeRate = decision.GetAbrilALUscoreFromSQL(stock, kospiList[stock], date)
                # open = int(stockPriceDF[i:i + 1]['open'])
                close = int(stockPriceDF[i:i + 1]['close'])
                # low = int(stockPriceDF[i:i + 1]['low'])
                # high = int(stockPriceDF[i:i + 1]['high'])

                tradeCnt = 0
                if descisionCode > 0 and stockCnt == 0:
                    tradeCnt = int(cashValue / close * tradeRate)
                elif descisionCode < 0 and stockCnt > 0:
                    tradeCnt = stockCnt

                stockCnt += (tradeCnt * descisionCode)
                cashValue -= close * abs(tradeCnt) * descisionCode
                stockValue = close * stockCnt

                # 4. 거래 이력 output
                # wr.writerow([date, descisionCode, stock, kospiList[stock], close, tradeCnt, stockValue, cashValue, (stockValue + cashValue)])
                print('날짜:', date,
                      'tradeRate:', tradeRate,
                      '거래유형:', descisionCode,
                      '종목코드:', stock,
                      '종목명:', kospiList[stock],
                      '거래가격:', close,
                      '거래수량:', tradeCnt,
                      '주식가치:', stockValue,
                      '현금자산:', cashValue,
                      '총자산:', stockValue + cashValue)

# f = open('/RPG/MoneyBot/output/' + str(datetime.date.today()) + '.csv', 'w', newline='')
# wr = csv.writer(f)
# wr.writerow(['날짜', '거래유형', '종목코드', '종목명', '거래가격', '거래수량', '주식가치', '현금자산', '총자산'])

for stock in portfolios:
    Trading.Simulation(stock=stock,
                       seedMoney=10000000,
                       fromDate='2017-01-01',
                       toDate='2017-12-31',
                       algorithmNumber=0)

# f.close()

# 4. 성과 분석
'''
input 파라미터 : 종목코드, 초기자본, 시뮬레이션 기간, 알고리즘 코드
'''



