#-*- coding:utf-8 -*-
import pandas as pd
import csv
import math
import RPG.PredictStock2.NewsCrawler as news
import RPG.PredictStock2.NaiveBayes as nb

def getStockData():
    fileName = 'data/가격정보(035720_카카오)_2017-04-25.csv'  # 2014.5.26 가격정보 이상

    stockData = open(fileName, 'r', encoding='euc-kr')
    reader = csv.reader(stockData)
    stockList = list(reader)
    # print(stockList[0])
    df = pd.DataFrame(stockList[1:])
    df.columns = stockList[0]
    df = df[df['시가'] != '']

    df['날짜'] = pd.to_datetime(df['날짜'])
    df['종가'] = pd.Series(df['종가'].str.replace(',', ''))
    df['시가'] = pd.Series(df['시가'].str.replace(',', ''))
    df['고가'] = pd.Series(df['고가'].str.replace(',', ''))
    df['저가'] = pd.Series(df['저가'].str.replace(',', ''))
    df['변동률'] = pd.Series(df['변동률'].str.replace(',', ''))
    # df = df.sort_values(by=['날짜'], ascending=[True])
    testDf = df[df['날짜'] >= '2016-01-01']
    return testDf

# 주식 데이터 가져오기
testDF = getStockData()
# print(testDF)

# for i in range(0, testDF.__len__()):
    # print(testDF['변동률'][i], ', ', math.log(float(testDF['변동률'][i]))*100)


article_list = news.crawl()
print(article_list)







