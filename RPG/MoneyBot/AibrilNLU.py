#-*- coding:utf-8 -*-

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
import RPG.MoneyBot.News as News
import datetime
import pandas as pd

def response(contentText='', targets=None):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        url='https://gateway.aibril-watson.kr/natural-language-understanding/api',
        username='7457e1d2-26a8-4b82-8f4d-782ad438ac10',
        password='ZSZ5Wmt8zRUA',
        version='2017-02-27')

    return natural_language_understanding.analyze(text=contentText, features=Features(sentiment=SentimentOptions(targets=[targets])))

def getScore(stockName, date):
    stockNewsList = News.crawl(stockName=stockName, date=date)
    decisionScore = 0
    for news in stockNewsList:
        # print(news)
        contentText, issueDatetime = News.get_content(news['link'])
        if contentText.__contains__(stockName) and issueDatetime > pd.to_datetime(str(date) + ' 15:30:00') + datetime.timedelta(days=-1) and issueDatetime < pd.to_datetime(str(date) + ' 15:30:00'):
            returnValue = response(contentText=contentText, targets=stockName)
            # print(returnValue)
            targetsScore = float(returnValue['sentiment']['targets'][0]['score'])
            documentScore = float(returnValue['sentiment']['document']['score'])

            decisionScore += (targetsScore + documentScore)/2

    return decisionScore


# print(json.dumps(NLU.response, indent=2))


