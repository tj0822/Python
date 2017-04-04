#-*- coding:utf-8 -*-

# 네이버 검색 Open API 예제
import json
import random
import urllib.request
import lxml
import webbrowser
from collections import Counter

# import pytagcloud
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

from bs4 import BeautifulSoup, NavigableString, Comment
from konlpy.tag import Kkma
from konlpy.utils import pprint
from numpy import *

import csv
import NaiveBayes


client_id = "RdEemi6FBrMzlIrFvrj3"
client_secret = "uCj3JBXkUV"
fileName = 'data/가격정보(035720_카카오)_2017-04-03.csv'       # 2014.5.26 가격정보 이상


stockData = open(fileName, 'r', encoding='euc-kr')
reader = csv.reader(stockData)
stockList = list(reader)
# print(stockList[0])
df = pd.DataFrame(stockList[1:])
df.columns = stockList[0]
df = df[df['시가'] != '']



df['날짜'] = pd.to_datetime(df['날짜'])
df['종가'] = pd.Series(df['종가'].str.replace(',', '')).astype(int)
df['시가'] = pd.Series(df['시가'].str.replace(',', '')).astype(int)
df['고가'] = pd.Series(df['고가'].str.replace(',', '')).astype(int)
df['저가'] = pd.Series(df['저가'].str.replace(',', '')).astype(int)

encText = urllib.parse.quote("카카오")
url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=100&sort=sim" # json 결과
# url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + "&display=10&sort=sim" # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()





docList = []
classList = []

if(rescode==200):
    response_body = response.read()
    j = json.loads(response_body.decode('utf-8'))

    # print(j)
    # print(response_body.decode('utf-8'))
    # print(j)
    # print(len(j["items"]))
    k = 0
    for i in range(0, len(j["items"])):
        # print('Title : ', j["items"][i]['title'])
        # print(j["items"][i]['originallink'])
        # print(j["items"][i]['link'])
        # print(j["items"][i]['description'])
        # print(j["items"][i]['pubDate'])

        # Beautiful Soup을 이용한 페이지
        # Crawling & Parsing
        targetUrl = j["items"][i]['link']
        if str(targetUrl).__contains__('http://news.naver.com'):
            # print(targetUrl)
            issueDate = datetime.datetime.strptime(j['items'][i]['pubDate'], "%a, %d %b %Y %H:%M:%S %z").date()
            afterDate = df[df['날짜'] >= issueDate].tail(1)['날짜']
            prevDate = df[df['날짜'] < issueDate].head(1)['날짜']
            soup = BeautifulSoup(urllib.request.urlopen(targetUrl).read(), "lxml")
            print('Title : ', soup.title.string)
            # print('게시일자', j['items'][i]['pubDate'])
            print('게시일자 : ', issueDate)
            # print('직후일자 : ', afterDate)
            # print('직전일자 : ', prevDate)
            print()

            # print(soup.prettify())
            # print(soup)
            newsbody = soup.find(id="articleBodyContents")
            # print(newsbody.contents)
            bodystr = ""
            try:
                for child in newsbody.children:
                    if (isinstance(child, NavigableString) and not isinstance(child, Comment)):
                        # print(child.string.strip())
                        bodystr += child.string.strip()

                # 형태소 분석
                kkma = Kkma()
                # pprint(kkma.nouns(bodystr))
                # pprint(kkma.pos(bodystr))
                wordList = kkma.nouns(bodystr)

                if k == 0:
                    testEntry = wordList
                    testIssueDate = issueDate
                    testTitle = soup.title.string
                else:
                    if (int(df[df['날짜'] >= issueDate].tail(1)['종가']) > int(df[df['날짜'] < issueDate].head(1)['종가'])):
                        print('up')
                        docList.append(wordList)
                        classList.append(1)
                    else:
                        if (int(df[df['날짜'] >= issueDate].tail(1)['종가']) < int(
                                df[df['날짜'] < issueDate].head(1)['종가'])):
                            print('down')
                            docList.append(wordList)
                            classList.append(0)
                        else:
                            print('hold')
                            docList.append(wordList)
                            classList.append(0)
                k += 1

            except:
                continue
        else:
            continue

    vocaList = NaiveBayes.createVocabList(docList)

    trainMat = []
    for postinDoc in docList:
        trainMat.append(NaiveBayes.setOfWords2Vec(vocaList, postinDoc))

    print('vocaList : ', vocaList)
    print('trainMat : ', trainMat)
    print('testEntry : ', testEntry)
    p0V, p1V, pAb = NaiveBayes.trainNB0(array(trainMat), array(classList))

    # testEntry = ['카카오', '인공지능', '알파고']
    thisDoc = array(NaiveBayes.setOfWords2Vec(vocaList, testEntry))
    print(testIssueDate, ' 일자의 ', testTitle, '기사 이후 주가는 ?\n', NaiveBayes.classifyNB(thisDoc, p0V, p1V, pAb))
else:
    print("Error Code:" + rescode)






