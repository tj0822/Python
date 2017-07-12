#-*- coding:utf-8 -*-

import pandas as pd
import datetime
from bs4 import BeautifulSoup, NavigableString, Comment, Tag
import urllib.request
from konlpy.tag import Kkma
import RPG.PredictStock.NaiveBayes as nb
import operator
import csv
import os
from numpy import *

tagList = ['NNG']

fileName = 'data/카카오_19991111~20170712.csv'

stockDF = pd.read_csv(fileName)
stockDF = stockDF.sort_values(by=['datetime'], ascending=[True])
# print(stockDF)
# print(stockDF.__len__())
# for item in stockDF.iterrows():
#     print(item[0], item[1]['datetime'], item[1]['close'])



vocaList = list()

kkma = Kkma()


def get_content(url):
    # print(url)
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
    # print(soup.prettify())
    content = soup.find(id="articleView")
    body = soup.find(id="realArtcContents")
    # print(body)
    # 제목
    # title = soup.find(id="articleSubecjt")
    # print(url)
    try:
        issueDatetime = content.em.contents[0]
        # 본문
        # 1차 : 기본방법
        con = ""
        try:
            for child in body.children:
                if (not isinstance(child, NavigableString) or isinstance(child, Comment)) or child.string is None or len(child.string.strip()) == 0:
                    continue
                con += child.string.strip() + '\r\n'
        except:
            pass

        # 2차 : <P> 태그 내의 값들을 출력
        if len(con.strip()) == 0:
            con = ''
            try:
                ps = body.find_all('p')
                for p in ps:
                    for str in p.stripped_strings:
                        if str is None or len(str) == 0:
                            continue

                        con += str + '\r\n'
            except:
                pass

        return con, issueDatetime
    except:
        pass

def crawl():
    def perdelta(start, end, delta):
        curr = start
        while curr < end:
            yield curr
            curr += delta

    base_url = "http://news.nate.com"
    # base_year = '2017'
    category = "eco"
    date = datetime.datetime.strptime(newsFromData, "%Y-%m-%d").date()
    lastDate = datetime.date.today()

    article_list = []
    article_cnt = 0

    # 기사 목록 추출
    for d in perdelta(date, lastDate, datetime.timedelta(days=1)):
        print(datetime.datetime.now(), ' : ', d)
        for i in range(1, getPageCount):
            target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + str(d).replace('-', '') + "&page=" + repr(i)
            soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
            # print(soup)
            titlebody = soup.find_all("ul")
            # print('titlebody : ', titlebody)
            postNoList = soup.findAll("div", {"class": "postNoList"})
            # print('classes :', postNoList.__len__())
            if postNoList.__len__() == 0:
                for item in titlebody:
                    if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
                        continue
                    for li_item in item.find_all("li"):
                        try:
                            item_title = li_item.a.contents[0].strip()

                            if str(item_title).__contains__(keyword):
                                # print(item_title)

                                item_link = base_url + li_item.a['href']
                                item_source = li_item.span.contents[0].strip()
                                article = {'title:': item_title,
                                           'link': item_link,
                                           'item_source': item_source}

                                yield article
                        except:
                            continue

            else:
                # print('기사 없음')
                break

newsList = crawl()

testSet = list()
trainingSet = list()
classList = list()
trainMat = list()

def getWords(wordList):
    for word in wordList:
        if(len(word[0]) > 1 and tagList.__contains__(word[1])):
            yield word[0]

def scoring(newsList):
    print('Scoring')
    for article in newsList:
        content, issueDateTime = get_content(article['link'])
        issueDateTime = pd.to_datetime(issueDateTime)
        issueDate = issueDateTime.date()
        issueTime = issueDateTime.time()
        wordList = getWords(kkma.pos(content))
        wordList = list(wordList)

        ws = set(wordList)
        dic = {}
        for word in ws:
            dic.update({word: wordList.count(word)})

        n = 10
        listDic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[:n]
        # print('listDic : ', listDic)
        # wordList.clear()

        topNWordList = list()
        for l in listDic:
            topNWordList.append(l[0])

        if issueTime >= pd.to_datetime('15:30:00').time():
            baseDate = stockDF[pd.to_datetime(stockDF['datetime']) > issueDate].head(1)['datetime']
        else:
            baseDate = stockDF[pd.to_datetime(stockDF['datetime']) >= issueDate].head(1)['datetime']

        # print('issueDate : ', issueDate)
        if issueDate >= pd.to_datetime(testSetFromDate).date() or len(baseDate) == 0:
            # test set
            # print('testSet')
            testSet.append({'issueDateTime': issueDateTime, 'wordList': topNWordList})
        else:
            # trainning set
            baseDate = pd.Series(baseDate).values[0]
            trainingSet.append({'issueDateTime': issueDateTime, 'wordList': topNWordList})
            todayPrice = int(stockDF[pd.to_datetime(stockDF['datetime']) == baseDate]['close'])
            prevPrice = int(stockDF[pd.to_datetime(stockDF['datetime']) < baseDate].tail(1)['close'])
            if (todayPrice > prevPrice):
                classList.append(1)
            else:
                if (todayPrice < prevPrice):
                    classList.append(0)
                else:
                    classList.append(0)


def Test():
    vocaList = nb.createVocabList(trainingSet)
    # print('vocaList : ', vocaList)
    for postinDoc in trainingSet:
        trainMat.append(nb.setOfWords2Vec(vocaList, postinDoc['wordList']))

    output_path = 'output_' + str(datetime.datetime.today().date())

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    vocaListFile = open(output_path + '/vocaListFile.csv', 'w')
    cw = csv.writer(vocaListFile, delimiter=',')
    cw.writerow(vocaList)
    vocaListFile.close()

    classListFile = open(output_path + '/classListFile.csv', 'w')
    cw = csv.writer(classListFile, delimiter=',')
    cw.writerow(classList)
    classListFile.close()

    trainMatFile = open(output_path + '/trainMatFile.csv', 'w')
    cw = csv.writer(trainMatFile, delimiter=',')
    cw.writerow(trainMat)
    trainMatFile.close()

    p0V, p1V, pAb = nb.trainNB0(array(trainMat), array(classList))

    resultFileName = output_path + '/output_' + str(datetime.datetime.today().date()) + '.csv'
    output = open(resultFileName, 'w')
    cw = csv.writer(output)

    for entry in testSet:
        thisDoc = array(nb.setOfWords2Vec(vocaList, entry['wordList']))
        result = nb.classifyNB(thisDoc, p0V, p1V, pAb)
        cw.writerow([entry['issueDateTime'], result])
        # print(entry['issueDateTime'], '기사 이후 주가는 ?\n', result)

    output.close()


keyword = '카카오'
newsFromData = '2017-01-01'
testSetFromDate = '2017-06-01'
getPageCount = 300

scoring(newsList)

Test()

