#-*- coding:utf-8 -*-

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
import RPG.MoneyBot.News as News
import datetime
import pandas as pd
import RPG.MoneyBot.MySQL as sql
import RPG.MoneyBot.Stock as Stock

def response(contentText='', targets=None):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        url='https://gateway.aibril-watson.kr/natural-language-understanding/api',
        username='7457e1d2-26a8-4b82-8f4d-782ad438ac10',
        password='ZSZ5Wmt8zRUA',
        version='2017-02-27')

    return natural_language_understanding.analyze(text=contentText, features=Features(sentiment=SentimentOptions(targets=[targets])))

def getScore(stockCode, stockName, date):
    stockNewsList = News.crawl(stockName=stockName, date=date)
    decisionScore = 0
    for news in stockNewsList:
        # print(news)
        contentText, issueDatetime = News.get_content(news['link'])
        if contentText.__contains__(stockName) and issueDatetime > pd.to_datetime(str(date) + ' 15:30:00') + datetime.timedelta(days=-1) and issueDatetime < pd.to_datetime(str(date) + ' 15:30:00'):
            returnValue = response(contentText=contentText, targets=stockName)
            print(returnValue)

            targetsScore = float(returnValue['sentiment']['targets'][0]['score'])
            documentScore = float(returnValue['sentiment']['document']['score'])
            query = "insert into aibril_alu(STOCK_CODE, url, text_characters, sentiment_targets, sentiment_document) VALUES ('%s', '%s', %d, %f, %f) " % (stockCode, news['link'], int(returnValue['usage']['text_characters']), targetsScore, documentScore)
            sql.insertStmt(query=query)

            decisionScore += (targetsScore + documentScore)/2

    return decisionScore


# print(json.dumps(NLU.response, indent=2))
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta



kospiList= Stock.GetKospi200()

# sql.insertStmt()


'''
코스피 200종목 뉴스에 대한 AIBRIL score migration
'''
fromDate = datetime.datetime.strptime('2000-01-01', "%Y-%m-%d").date()
toDate = datetime.datetime.strptime('2018-12-01', "%Y-%m-%d").date()
for stockCode in kospiList.keys():
    # print(getScore(stock, '카카오', datetime.datetime.strptime('2018-01-11', "%Y-%m-%d").date()))
    for d in perdelta(fromDate, toDate, datetime.timedelta(days=1)):
        getScore(stockCode, kospiList[stockCode], d)


