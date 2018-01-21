#-*- coding:utf-8 -*-
import RPG.MoneyBot.AibrilNLU as alu
import random

# -1: sell 0:stay 1:buy
def GetAbrilALUscore(stock, stockName, date):
    score = alu.getScore(stock, stockName, date)
    decisionCode = 0
    tradeRate = 0
    if score > 0:
        decisionCode = 1
    elif score < 0:
        decisionCode = -1
    else:
        pass

    tradeRate = score

    return decisionCode, tradeRate


import RPG.MoneyBot.MySQL as sql
import pandas as pd
import datetime
def GetAbrilALUscoreFromSQL(stock, stockName, date):
    fromDate = pd.to_datetime(str(date) + ' 15:30:00') + datetime.timedelta(days=-1)
    toDate = pd.to_datetime(str(date) + ' 15:30:00')
    # query = "SELECT AVG(sentiment_targets), AVG(sentiment_document) FROM aibril_alu WHERE CODE = '%s' and issueDatetime >= '%s' and issueDatetime < '%s' " % stock,  str(fromDate), str(toDate)
    query = "SELECT AVG(sentiment_targets), AVG(sentiment_document) FROM aibril_alu WHERE STOCK_CODE = '%s' and issueDatetime >= '%s' and issueDatetime < '%s' " %(stock, fromDate, toDate)
    result = sql.selectStmt(query)
    # print(result[0][0])
    # print(result[0][1])
    decisionCode = 0
    score = 0

    if result[0][0] is not None and result[0][1] is not None:
        score = float(result[0][0]) + float(result[0][1])

    if score > 0:
        decisionCode = 1
    elif score < 0:
        decisionCode = -1
    else:
        pass

    return decisionCode, score

def GetRandomScore(stock, stockName, date):
    return random.randrange(-1, 2)          # -1이상 2미만

#
