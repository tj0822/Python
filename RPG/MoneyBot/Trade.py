#-*- coding:utf-8 -*-

import datetime
import RPG.MoneyBot.MySQL as sql
import pandas as pd
import RPG.MoneyBot.MakeDecision as decision

def Simulation(stockCode=None, stockName=None, seedMoney=1000000, fromDate='2017-01-01', toDate='2018-12-31', algorithmNumber=0):
    fromSimulDate = datetime.datetime.strptime(str(fromDate), "%Y-%m-%d").date()
    toSimulDate = datetime.datetime.strptime((str(toDate)), "%Y-%m-%d").date()
    cashValue = seedMoney
    stockCnt = 0
    # 가격데이터 가져오기(나중에 DB select로 변경 예정)
    # stockPriceDF = pd.read_csv(stockDirectory + stock + '_' + kospiList[stock] + '.csv').sort_values(['datetime'])

    stockPriceDF = GetStockPrice(stockCode)

    for i in range(0, len(stockPriceDF)):
        # date = datetime.datetime.strptime(stockPriceDF[i:i + 1]['datetime'].values[0], "%Y-%m-%d").date()
        date = stockPriceDF[i:i + 1]['datetime'].values[0]
        volume = int(stockPriceDF[i:i + 1]['volume'])
        if date >= fromSimulDate and (int(stockPriceDF[i - 1:i]['volume']) * volume) > 0 and date <= toSimulDate:

            '''#########################################################################################'''
            '''일자별 의사결정: 매수/매도/Holding'''
            descisionCode, tradeRate = decision.GetAbrilAluScore(stockCode, stockName, date, 0)         # 이부분을 코딩한 알고리즘으로 교체하면 됨(거래유형과 거래비율 결정)  0 : AVG, 1 : SUM
            '''#########################################################################################'''

            # open = int(stockPriceDF[i:i + 1]['open'])
            close = int(stockPriceDF[i:i + 1]['close'])
            # low = int(stockPriceDF[i:i + 1]['low'])
            # high = int(stockPriceDF[i:i + 1]['high'])

            tradeCnt = 0        # 0 ~ 1 사이여야함(거래 비율) : 0이면 거래 안함 1이면 보유현금의 100% 한도까지 거래

            if descisionCode > 0:
                # 매수
                tradeCnt = int(cashValue / close * min(tradeRate, 1))
            elif descisionCode < 0 and stockCnt > 0:
                # 매도
                tradeCnt = stockCnt * descisionCode

            stockCnt += tradeCnt
            cashValue -= close * tradeCnt
            stockValue = close * stockCnt

            # 4. 거래 이력 output
            # wr.writerow([date, descisionCode, stock, kospiList[stock], close, tradeCnt, stockValue, cashValue, (stockValue + cashValue)])
            print('날짜:', date,
                  'tradeRate:', tradeRate,
                  '거래유형:', descisionCode,
                  '종목코드:', stockCode,
                  '종목명:', stockName,
                  '거래가격:', close,
                  '거래수량:', tradeCnt,
                  '주식가치:', stockValue,
                  '현금자산:', cashValue,
                  '총자산:', stockValue + cashValue)

def GetStockPrice(stockCode=None):
    query = "SELECT CODE, DATE, PRICE_START, PRICE_HIGH, PRICE_LOW, PRICE_END, TRADE_AMOUNT FROM stock_price WHERE CODE = '%s' ORDER BY DATE" % stockCode
    df = pd.DataFrame(sql.selectStmt(query))
    df.columns = ['stockcode', 'datetime', 'close', 'high', 'low', 'open', 'volume']

    return df