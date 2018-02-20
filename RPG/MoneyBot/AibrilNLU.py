# -*- coding:utf-8 -*-

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
import RPG.MoneyBot.News as News
import datetime
import pandas as pd
import RPG.MoneyBot.MySQL as sql
import RPG.MoneyBot.Stock as Stock


def response(contentText='', targets=None):
    # tj0822@hotmail.com
    # natural_language_understanding = NaturalLanguageUnderstandingV1(
    #     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    #     username='c6a84ec0-1e83-4b7d-bd5e-d614646dca86',
    #     password='otKb7OXpjOPB',
    #     version='2017-02-27')

    # tj820822@gmail.com
    # natural_language_understanding = NaturalLanguageUnderstandingV1(
    #     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    #     username='a6223f98-a1cb-4738-b33d-1ebea0a3908b',
    #     password='gS0hVasrhobO',
    #     version='2017-02-27')

    # tj0822@naver.com
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        url='https://gateway.watsonplatform.net/natural-language-understanding/api',
        username='9867d1d9-263a-4272-a397-5a34269cb0d6',
        password='KikuNeCyvYzN',
        version='2017-02-27')

    # tj0822@daum.net
    # natural_language_understanding = NaturalLanguageUnderstandingV1(
    #     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    #     username='742a3873-b5b3-4fe6-afed-5fc07e0b0e58',
    #     password='XWS8s1hyoVhV',
    #     version='2017-02-27')

    # tj0822@hanmail.net
    # natural_language_understanding = NaturalLanguageUnderstandingV1(
    #     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    #     username='e5843677-a4bc-4cda-bb6b-385661a19ae8',
    #     password='WJkgDdbXBMW2',
    #     version='2017-02-27')
    try:
        return natural_language_understanding.analyze(text=contentText, features=Features(sentiment=SentimentOptions(targets=[targets])))
    except:
        return None

def getScore(stockCode, stockName, date):
    stockNewsList = News.crawl(stockName=stockName, date=date)
    decisionScore = 0
    for news in stockNewsList:
        contentText, issueDatetime = News.get_content(news['link'])
        # if contentText is not None and contentText.__contains__(stockName) and issueDatetime > pd.to_datetime(str(date) + ' 15:30:00') + datetime.timedelta(days=-1) and issueDatetime < pd.to_datetime(str(date) + ' 15:30:00'):
        if contentText is not None and contentText.__contains__(stockName):

            chkQuery = "SELECT news_title, item_source, issueDatetime, text_characters, sentiment_targets, sentiment_document, stock_code FROM aibril_alu WHERE url = '%s' and stock_code <> '%s' LIMIT 1" % (news['link'], stockCode)
            chkResult = sql.selectStmt(chkQuery)
            if chkResult.__len__() == 0:
                returnValue = response(contentText=contentText, targets=stockName)
                if returnValue == None:
                    return 0.0
                news_title = news['title']
                item_source = news['item_source']
                text_characters = int(returnValue['usage']['text_characters'])
                targetsScore = float(returnValue['sentiment']['targets'][0]['score'])
                documentScore = float(returnValue['sentiment']['document']['score'])
            else:
                news_title = chkResult[0][0]
                item_source = chkResult[0][1]
                issueDatetime = chkResult[0][2]
                text_characters = int(chkResult[0][3])
                targetsScore = float(chkResult[0][4])
                documentScore = float(chkResult[0][5])

            query = "insert into aibril_alu(STOCK_CODE, url, news_title, item_source, issueDatetime, text_characters, sentiment_targets, sentiment_document) VALUES ('%s', '%s', '%s', '%s', '%s', %d, %f, %f) " % (stockCode, news['link'], str(news_title).replace("'", "''"), item_source, str(issueDatetime), text_characters, targetsScore, documentScore)
            sql.insertStmt(query=query)
            decisionScore += (targetsScore + documentScore)/2

    return decisionScore


# print(json.dumps(NLU.response, indent=2))
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta


'''
코스피 200종목 뉴스에 대한 AIBRIL score migration
'''
import mysql.connector
kospiList= Stock.GetKospi200()

# conn = mysql.connector.connect(user='python', password='python',
#                               host='13.124.46.173',
#                               database='stock')


# fromDate = datetime.datetime.strptime('2011-10-18', "%Y-%m-%d").date()
# toDate = datetime.datetime.strptime('2018-12-01', "%Y-%m-%d").date()
# for stockCode in kospiList.keys():
#     # print(getScore(stock, '카카오', datetime.datetime.strptime('2018-01-11', "%Y-%m-%d").date()))
#     if stockCode == '005930' or stockCode == '000660':
#         pass
#         # for d in perdelta(fromDate, toDate, datetime.timedelta(days=1)):
#         #     print(d, stockCode, kospiList[stockCode])
#         #     getScore(stockCode, kospiList[stockCode], d)
#         #     conn.commit()
#     elif stockCode == '005380':
#         fromDate = datetime.datetime.strptime('2017-02-22', "%Y-%m-%d").date()
#         toDate = datetime.datetime.strptime('2018-12-01', "%Y-%m-%d").date()
#         for d in perdelta(fromDate, toDate, datetime.timedelta(days=1)):
#             print(d, stockCode, kospiList[stockCode])
#             getScore(stockCode, kospiList[stockCode], d)
#             conn.commit()
#     else:
#         fromDate = datetime.datetime.strptime('2017-01-01', "%Y-%m-%d").date()
#         toDate = datetime.datetime.strptime('2018-12-01', "%Y-%m-%d").date()
#         for d in perdelta(fromDate, toDate, datetime.timedelta(days=1)):
#             print(d, stockCode, kospiList[stockCode])
#             getScore(stockCode, kospiList[stockCode], d)
#             conn.commit()
#
# conn.close()

# fromDate = datetime.datetime.strptime('2005-03-01', "%Y-%m-%d").date()


def getScoreByDate(news, stockCode, stockName):
    contentText, issueDatetime = News.get_content(news['link'])
    if contentText is not None and contentText.__contains__(stockName):

        # chkQuery = "SELECT news_title, item_source, issueDatetime, text_characters, sentiment_targets, sentiment_document, stock_code FROM aibril_alu WHERE url = '%s' and stock_code <> '%s' LIMIT 1" % (news['link'], stockCode)
        chkQuery = "SELECT news_title, item_source, issueDatetime, text_characters, sentiment_targets, sentiment_document, stock_code FROM aibril_alu WHERE url = '%s' LIMIT 1" % (news['link'])
        chkResult = sql.selectStmt(chkQuery)
        if chkResult.__len__() == 0:
            returnValue = response(contentText=contentText, targets=stockName)
            if returnValue == None:
                return 0.0
            news_title = news['title']
            item_source = news['item_source']
            text_characters = int(returnValue['usage']['text_characters'])
            targetsScore = float(returnValue['sentiment']['targets'][0]['score'])
            documentScore = float(returnValue['sentiment']['document']['score'])
        else:
            news_title = chkResult[0][0]
            item_source = chkResult[0][1]
            issueDatetime = chkResult[0][2]
            text_characters = int(chkResult[0][3])
            targetsScore = float(chkResult[0][4])
            documentScore = float(chkResult[0][5])

        query = "insert into aibril_alu(STOCK_CODE, url, news_title, item_source, issueDatetime, text_characters, sentiment_targets, sentiment_document) VALUES ('%s', '%s', '%s', '%s', '%s', %d, %f, %f) " % (stockCode, news['link'], str(news_title).replace("'", "''"), item_source, str(issueDatetime), text_characters, targetsScore, documentScore)
        sql.insertStmt(query=query)





# fromDate = datetime.datetime.strptime('2018-01-11', "%Y-%m-%d").date()
# toDate = datetime.datetime.strptime('2018-12-31', "%Y-%m-%d").date()
#
# for d in perdelta(fromDate, toDate, datetime.timedelta(days=1)):
#     print(d)
#     newsList = News.crawlByStockNameList(list(kospiList.values()), d)
#     for news in newsList:
#         for stockCode in kospiList.keys():
#             if stockCode == '005930':
#                 continue
#             # elif stockCode == '000660' or stockCode == '005380' or stockCode == '005490' or stockCode == '012330' or stockCode == '032830' or stockCode == '035420' or stockCode == '051910' or stockCode == '105560':
#                 # toDate = datetime.datetime.strptime('2016-12-31', "%Y-%m-%d").date()
#                 # continue
#             else:
#                 stockName = str(kospiList[stockCode])
#                 if str(news['title']).__contains__(stockName):
#                     print(news)
#                     getScoreByDate(news, stockCode, kospiList[stockCode])
