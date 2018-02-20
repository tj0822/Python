#-*- coding:utf-8 -*-
import RPG.MoneyBot.AibrilNLU as alu
import random
import RPG.MoneyBot.MySQL as sql
import pandas as pd
import datetime

def GetAbrilALUscoreByNews(stock, stockName, date):
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

def GetAbrilAluSumAvg(stock, stockName, date):
    fromDate = pd.to_datetime(str(date) + ' 15:30:00') + datetime.timedelta(days=-1)
    toDate = pd.to_datetime(str(date) + ' 15:30:00')
    query = "SELECT SUM(sentiment_targets), SUM(sentiment_document), AVG(sentiment_targets), AVG(sentiment_document) FROM aibril_alu WHERE STOCK_CODE = '%s' and issueDatetime >= '%s' and issueDatetime < '%s' " % (stock, fromDate, toDate)
    result = sql.selectStmt(query)

    return result

def GetAbrilAluScore(stock, stockName, date, flag):
    result = GetAbrilAluSumAvg(stock, stockName, date)
    decisionCode = 0
    score = 0

    if result[0][0] is not None and result[0][1] is not None:
        if flag == 1:
            score = (float(result[0][0]) + float(result[0][1])) / 2
        elif flag == 0:
            score = (float(result[0][2]) + float(result[0][3])) / 2

    if score > 0:
        decisionCode = 1
    elif score < 0:
        decisionCode = -1
    else:
        pass

    return decisionCode, score

def GetRandomScore(stock, stockName, date):
    descionCode = random.randrange(-1, 2)       # -1이상 2미만
    tradeRate = 1
    return descionCode, tradeRate


