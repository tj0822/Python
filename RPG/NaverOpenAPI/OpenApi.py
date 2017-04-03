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

import csv


client_id = "RdEemi6FBrMzlIrFvrj3"
client_secret = "uCj3JBXkUV"
fileName = '가격정보(035720_카카오)_enc.csv'       # 2014.5.26 가격정보 이상


stockData = open(fileName, 'r', encoding='utf-8')
reader = csv.reader(stockData)
stockList = list(reader)
# print(stockList[0])
df = pd.DataFrame(stockList[1:])
df.columns = stockList[0]
print(df.columns)
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


if(rescode==200):
    response_body = response.read()
    j = json.loads(response_body.decode('utf-8'))
    # print(j)
    # print(response_body.decode('utf-8'))
    # print(j)
    # print(len(j["items"]))
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
            prevDate = issueDate + relativedelta(days=-1)

            soup = BeautifulSoup(urllib.request.urlopen(targetUrl).read(), "lxml")
            print('Title : ', soup.title.string)
            # print('게시일자', j['items'][i]['pubDate'])
            print('게시일자 : ', issueDate)

            print()

            if (df[df['날짜'] == str(issueDate)]['종가'] > df[df['날짜'] == str(prevDate)]['종가']):
                print('up')
            else:
                if (df[df['날짜'] == str(issueDate)]['종가'] < df[df['날짜'] == str(prevDate)]['종가']):
                    print('down')
                else:
                    print('hold')

            # print(soup.prettify())
            # print(soup)
            newsbody = soup.find(id="articleBodyContents")
            # print(newsbody.contents)
            bodystr = ""
            for child in newsbody.children:
                if (isinstance(child, NavigableString) and not isinstance(child, Comment)):
                    # print(child.string.strip())
                    bodystr += child.string.strip()

            # 형태소 분석
            kkma = Kkma()
            # pprint(kkma.nouns(bodystr))
            # pprint(kkma.pos(bodystr))
        else:
            continue
else:
    print("Error Code:" + rescode)



# Word Cloud
# def get_tags(text, ntags=50, multiplier=10):
# #    h = Hannanum()
#     nouns = text
#     count = Counter(nouns)
#     return [{'color': color(), 'tag': n, 'size': c*multiplier} for n, c in count.most_common(ntags)]

# def draw_cloud(tags, filename, fontname='Ngulim', size=(800, 600)):
#     pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
#     webbrowser.open(filename)

# r = lambda: random.randint(0,255)
# color = lambda: (r(), r(), r())
# tags = get_tags(kkma.nouns(bodystr))
# draw_cloud(tags, "wordcloud.jpg")

