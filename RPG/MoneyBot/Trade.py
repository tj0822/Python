#-*- coding:utf-8 -*-

import datetime
import RPG.MoneyBot.MySQL as sql
import pandas as pd
import RPG.MoneyBot.MakeDecision as decision
import RPG.MoneyBot.SelctStocks as select

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

def Simulation2(seedMoney=10000000, fromDate='2017-01-01', toDate='2017-12-31'):
    fromSimulDate = datetime.datetime.strptime(str(fromDate), "%Y-%m-%d").date()
    toSimulDate = datetime.datetime.strptime((str(toDate)), "%Y-%m-%d").date()
    cashValue = seedMoney
    portfolio = dict()

    for d in perdelta(fromSimulDate, toSimulDate + datetime.timedelta(days=1), datetime.timedelta(days=1)):
        if(portfolio.__len__() > 0):
            for stock in list(portfolio):
                query =   "SELECT STOCK_CODE, (AVG(sentiment_targets) + AVG(sentiment_document)) / 2  " \
                          "                    FROM aibril_alu " \
                          "                   WHERE issueDatetime >= '%s' " \
                          "                     AND issueDatetime < '%s' " \
                          "                     AND STOCK_CODE = '%s'	" \
                          "                GROUP BY STOCK_CODE" %(pd.to_datetime(str(d + datetime.timedelta(days=-1)) + ' 15:30:00'), pd.to_datetime(str(d) + ' 15:30:00'), stock)
                result = sql.selectStmt(query)

                if len(result) > 0:
                    tradeRate = result[0][1]
                    if tradeRate < 0:
                        stockPrice = GetStockPriceByDate(stock, d)
                        if len(stockPrice) > 0:  # 가격이 있을 때만
                            print('매도 :', stock, stockPrice[0][5], portfolio[stock])
                            cashValue += stockPrice[0][5] * portfolio[stock]
                            portfolio.pop(stock)

        else:
            buyStock = select.GetStockByAibrilScore(datetime.datetime.strptime(str(d), "%Y-%m-%d").date())[0]
            stockCode = buyStock[0]
            tradeRate = buyStock[1]
            stockPrice = GetStockPriceByDate(stockCode, d)
            if len(stockPrice) > 0:     # 가격이 있을 때만
                if tradeRate > 0:
                    close = stockPrice[0][5]
                    # tradeCnt = int(min(cashValue, 1000000) / close * min(tradeRate, 1))
                    tradeCnt = int(min(cashValue, cashValue) / close)
                    if tradeCnt > 0:
                        if portfolio.__contains__(stockCode):
                            portfolio[stockCode] += tradeCnt
                        else:
                            portfolio[stockCode] = tradeCnt
                        cashValue -= close * tradeCnt
                        print('매수 :', stockCode, close, tradeCnt)

        stockValue = 0
        for stock in portfolio:
            stockValue += portfolio[stock] * GetStockLastPrice(stock, d)[0][0]
        print(d, portfolio, cashValue, stockValue, cashValue+stockValue)

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

def GetStockPrice(stockCode=None):
    query = "SELECT CODE, DATE, PRICE_START, PRICE_HIGH, PRICE_LOW, PRICE_END, TRADE_AMOUNT FROM stock_price WHERE CODE = '%s' ORDER BY DATE" % stockCode
    df = pd.DataFrame(sql.selectStmt(query))
    df.columns = ['stockcode', 'datetime', 'close', 'high', 'low', 'open', 'volume']

    return df

def GetStockPriceByDate(stockCode=None, date=None):
    query = "SELECT CODE, DATE, PRICE_START, PRICE_HIGH, PRICE_LOW, PRICE_END, TRADE_AMOUNT FROM stock_price WHERE CODE = '%s' and DATE = '%s' " % (stockCode, date)
    return sql.selectStmt(query)

def GetStockLastPrice(stockCode=None, date=None):
    query = "SELECT PRICE_END FROM stock_price WHERE CODE = '%s' and DATE <= '%s' ORDER BY DATE DESC LIMIT 0, 1 " % (stockCode, date)
    return sql.selectStmt(query)

Simulation2()