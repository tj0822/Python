#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import ssl
import RPG.PredictStock.MySQL as sql

def GetKospi200():
    stockDic = dict()
    lastPageNum = 0

    # 마지막 페이지 찾기
    base_url = "http://finance.naver.com/sise/entryJongmok.nhn?&page="
    target_url = base_url + str(1)
    context = ssl._create_unverified_context()
    # soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
    soup = BeautifulSoup(urllib.request.urlopen(target_url, context=context).read().decode('euc-kr', 'ignore'), "lxml")
    for item in soup.find_all('td'):
        if item.has_attr('class') and 'pgRR' in item['class']:
            lastPageNum = int(str(item.a['href']).replace('/sise/entryJongmok.nhn?&page=', ''))
1
    for i in range(1, lastPageNum+1):
        target_url = base_url + str(i)
        # soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
        soup = BeautifulSoup(urllib.request.urlopen(target_url, context=context).read().decode('euc-kr', 'ignore'), "lxml")
        postNoList = soup.find_all('a')


        # 종목코드와 종목명 담기
        for item in postNoList:
            if item.has_attr('target') and '_parent' in item['target'] and item.has_attr('href'):
                if str(item['href']).startswith('/item/main.nhn?code='):
                    stockDic[str(item['href']).replace('/item/main.nhn?code=', '')] = item.text
    return stockDic





# stockDict = GetKospi200()
# print(stockDict)
# stockCodeList = list(stockDict.keys())
# print(stockCodeList)
# stockNameList = list(stockDict.values())

# for key in stockDict:
    # print(key, stockDict[key])
    # query = "insert into stock_kospi200(stock_code, stock_name, crawling_date) VALUES ('%s', '%s', NOW()) " % (key, stockDict[key])
    # print(query,';')
    # sql.insertStmt(query=query)
