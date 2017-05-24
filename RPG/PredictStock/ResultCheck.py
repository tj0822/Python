#-*- coding:utf-8 -*-

import csv
import pandas as pd

class Stock:
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

        df = df.sort_values(by=['날짜'], ascending=[True])
        # df = df[df['날짜'] >= '2016-01-01']
        return df

stockDF = Stock.getStockData()

outputFileName = 'output_2017-05-22.csv'
stockData = open(outputFileName, 'r', encoding='euc-kr')
reader = csv.reader(stockData)
outputList = list(reader)

# outputDF = pd.DataFrame(list(reader))
# outputDF.columns = ['issueDateTime', 'result']

trueCnt = 0
falseCnt = 0

baseDate = ''
for r in outputList:

    issueDateTime = pd.to_datetime(r[1])
    # print(pd.to_datetime(r[0]).time())
    if issueDateTime.time() > pd.to_datetime('15:30:00').time():
        # print('장 마감 이후')
        baseDate = stockDF[stockDF['날짜'] > issueDateTime.date()].head(1)['날짜']
    else:
        # print('장 마감 이전')
        baseDate = stockDF[stockDF['날짜'] >= issueDateTime.date()].head(1)['날짜']

    try:
        baseDate = pd.to_datetime(baseDate.values[0]).date()

        todayPrice = int(stockDF[stockDF['날짜'] == baseDate]['종가'])
        prevPrice = int(stockDF[stockDF['날짜'] < baseDate].tail(1)['종가'])

        if(todayPrice > prevPrice):
            r.append('1')
        else:
            r.append('0')

        print(r)
        if(str(r[2]).replace(' ', '') == r[3]):
            trueCnt += 1
        else:
            falseCnt += 1
        # print('issueDateTime : ', issueDateTime, ' baseDate : ', baseDate, '당일 종가 :', todayPrice, ' 전날 종가 : ', prevPrice)
    except:
        pass

print(outputList)
print('trueCnt : ', trueCnt)
print('falseCnt : ', falseCnt)
# baseDate = ''
# if issueTime > pd.to_datetime('15:30:00').time():
#     # print('장 마감 이후')
#     baseDate = stockDF[stockDF['날짜'] > issueDate].head(1)['날짜']
# else:
#     # print('장 마감 이전')
#     baseDate = stockDF[stockDF['날짜'] >= issueDate].head(1)['날짜']

# print(outputDF)