#-*- coding:utf-8 -*-
import datetime
from bs4 import BeautifulSoup
import urllib.request
from konlpy.tag import Kkma
import pandas as pd


print('start time : ', datetime.datetime.now())


''' 종목 리스트 가져오기 '''
def GetKospiList():
    stockDic = dict()
    lastPageNum = 0

    # 마지막 페이지 찾기
    base_url = "http://finance.naver.com/sise/sise_market_sum.nhn?&page="
    target_url = base_url + str(1)
    soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
    for item in soup.find_all('td'):
        if item.has_attr('class') and 'pgRR' in item['class']:
            # print(int(str(item.a['href']).replace('/sise/sise_market_sum.nhn?&page=', '')))
            lastPageNum = int(str(item.a['href']).replace('/sise/sise_market_sum.nhn?&page=', ''))




    for i in range(1, lastPageNum+1):
        target_url = base_url + str(i)
        soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
        postNoList = soup.find_all('a')

        # 종목코드와 종목명 담기
        for item in postNoList:
            if item.has_attr('class') and item.has_attr('href'):
                if str(item['href']).startswith('/item/main.nhn?code='):
                    stockDic[str(item['href']).replace('/item/main.nhn?code=', '')] = item.text
    return stockDic

# print(GetKospiList().values())

stockDict = GetKospiList()
stockCodeList = list(stockDict.keys())
stockNameList = list(stockDict.values())


stockDataFrame = pd.DataFrame(columns=('code', 'name', 'date', 'count'))


newsFromDate = '2017-01-01'
newsToDate = datetime.date.today()
getPageCount = 300
kkma = Kkma()


class NateNews:
    def crawl(self):
        def perdelta(start, end, delta):
            curr = start
            while curr < end:
                yield curr
                curr += delta

        base_url = "http://news.nate.com"
        # base_year = '2017'
        category = "eco"
        date = datetime.datetime.strptime(newsFromDate, "%Y-%m-%d").date()


        # 기사 목록 추출
        for d in perdelta(date, newsToDate, datetime.timedelta(days=1)):
            print(datetime.datetime.now(), ' : ', d)

            stockMatList = [0] * len(stockNameList)

            for i in range(1, getPageCount):
                target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + str(d).replace('-', '') + "&page=" + repr(i)
                soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")

                for item in soup.find_all("ul"):

                    if item.has_attr('class') and 'mduSubject' in item['class']:
                        for li_item in item.find_all('li'):

                            title = li_item.a.text
                            wordList = kkma.nouns(title)
                            for item in wordList:
                                if(stockNameList.__contains__(item)):
                                    stockMatList[stockNameList.index(item)] += 1

            tempDataFrame = pd.DataFrame(columns=('code', 'name', 'date', 'count'))
            # print(tempDataFrame.columns)
            tempDataFrame['code'] = stockCodeList
            tempDataFrame['name'] = stockNameList
            tempDataFrame['date'] = str(d)
            tempDataFrame['count'] = stockMatList

            # print(tempDataFrame)

            global stockDataFrame
            stockDataFrame = stockDataFrame.append(tempDataFrame, ignore_index= True)

            # print(stockDataFrame)

news = NateNews()
news.crawl()


# print(stockDataFrame.sort(columns='Count', ascending=False))
outputFileName = 'output/output_'+ newsFromDate + '~' + str(datetime.date.today()) + '.csv'
stockDataFrame.to_csv(outputFileName, index=False)


print('end time : ', datetime.datetime.now())

# d = ['삼성', 'LG', '로또', '카카오']
# for item in GetKospiList().values():
#     if (d.__contains__(item)):
#         print(item, ' 존재')
#     else:
#         print(item, ' 없음')