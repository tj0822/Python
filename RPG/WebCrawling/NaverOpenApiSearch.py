#-*- coding:utf-8 -*-

# 네이버 검색 Open API 예제
import os
import sys
import json

import urllib.request

from bs4 import BeautifulSoup

# 모듬 문서에 있는 모든 유일한 단어 목록을 생성(set)
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        print(document)
        vocabSet = vocabSet | set(document)         # | : 집합 유형 변수 합치기
    return list(vocabSet)


client_id = "RdEemi6FBrMzlIrFvrj3"
client_secret = "uCj3JBXkUV"
encText = urllib.parse.quote("박근혜")
url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=100&sort=sim" # json 결과
# url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + "&display=10&sort=sim" # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()


if(rescode==200):
    response_body = response.read()
    j = json.loads(response_body.decode('utf-8'))
    # print(response_body.decode('utf-8'))
    # print(len(j["items"]))
    for i in range(0, len(j["items"])):
        # print(j["items"][i]['title'])
        # print(j["items"][i]['originallink'])
        # print(j["items"][i]['link'])
        # print(j['items'][i]['description'])
        print(j['items'][i]['pubDate'])


        newsURL = j["items"][i]['link']
        newsRequest = urllib.request.Request(newsURL)
        newsResponse = urllib.request.urlopen(newsRequest)
        newsResponse_body = newsResponse.read()
        soup = BeautifulSoup(newsResponse_body, 'html.parser')

        if newsURL.__contains__('news.naver.com'):
            print(soup.title.string)
            print(j['items'][i]['pubDate'])

            if str(soup.find(id='articleBodyContents')) != 'None':
                # print(soup.find(id = 'articleBodyContents'))
                document = str(soup.find(id = 'articleBodyContents'))
                print(document.split())
                # wordList = createVocabList(document)
                # print(wordList)
            else :
                if str(soup.find(id='articleBody')) != 'None':
                    # print(soup.find(id='articleBody'))
                    document = str(soup.find(id='articleBody'))
                    print(document.split())
                    # wordList = createVocabList(document)
                    # print(wordList)

        # print(soup.body.string)
        print("")
else:
    print("Error Code:" + rescode)




