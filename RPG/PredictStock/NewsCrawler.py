import urllib.request
from bs4 import BeautifulSoup, NavigableString, Comment, Tag
import time
# import pymssql
import numpy as np
import pandas as pd
import datetime
from time import localtime, strftime
import sqlite3
from konlpy.tag import Kkma
from konlpy.utils import pprint
import csv
import RPG.PredictStock.NaiveBayes as nb
from numpy import *
import os

tagList = ['NNG', 'NNP', 'NNB', 'NNM', 'VV', 'VA', 'VXV', 'UN']

class Stock:
    def getStockData(self):
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


class NateNews:


    # def get_article(self, category, base_url, base_year, date, page):
    #     list = []
    #     target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + date + "&page=" + repr(page)
    #     # print(target_url)
    #     soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
    #     # print(soup.prettify())
    #     titlebody = soup.find_all("ul")
    #     for item in titlebody:
    #         if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
    #             continue
    #         for li_item in item.find_all("li"):
    #             item_title = li_item.a.contents[0].strip()
    #
    #             if str(item_title).__contains__(keyword):
    #                 # print(item_title)
    #                 item_link = base_url + li_item.a['href']
    #                 item_source = li_item.span.contents[0].strip()
    #                 item_changed = time.strptime(base_year + '-' + li_item.em.contents[0], '%Y-%m-%d %H:%M')
    #                 list.append((item_title, item_link, item_source, item_changed))
    #
    #             # print([item_title, item_link, item_source, item_changed])
    #             # print('Title : ' + item_title)
    #     # print('Link : ' + item_link)
    #     #        print('Source : ' + item_source)
    #     #        print('Changed : ' + item_changed)
    #     return list


    def get_article(self, category, base_url, date, page):
        list = []
        target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + date + "&page=" + repr(page)
        # print(target_url)
        soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
        # print(soup.prettify())
        titlebody = soup.find_all("ul")
        for item in titlebody:
            if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
                continue
            for li_item in item.find_all("li"):
                item_title = li_item.a.contents[0].strip()

                if str(item_title).__contains__(keyword):
                    item_link = base_url + li_item.a['href']
                    item_source = li_item.span.contents[0].strip()
                    # item_changed = time.strptime(li_item.em.contents[0], '%Y-%m-%d %H:%M')
                    # list.append((item_title, item_link, item_source, item_changed))
                    list.append((item_title, item_link, item_source))
                    # print([item_title, item_link, item_source, item_changed])
                    # print('Title : ' + item_title)
        # print('Link : ' + item_link)
        #        print('Source : ' + item_source)
        #        print('Changed : ' + item_changed)
        return list

    def get_article_generator(self, category, base_url, date, page):
        target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + date + "&page=" + repr(page)
        print(target_url)
        soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")

        print(soup.prettify())
        titlebody = soup.find_all("ul")
        for item in titlebody:
            if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
                continue
            for li_item in item.find_all("li"):
                item_title = li_item.a.contents[0].strip()

                if str(item_title).__contains__(keyword):
                    item_link = base_url + li_item.a['href']
                    item_source = li_item.span.contents[0].strip()
                    article = {'link':item_link,
                               'news_source':item_source}
                    print(article)
                    yield article

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
                    # print(child)
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
                            # print(str)
                            con += str + '\r\n'
                except:
                    pass

            return con, issueDatetime
        except:
            pass

    def get_content2(self, url):
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
        # print(soup.prettify())
        content = soup.find(id="articleView")
        body = soup.find(id="realArtcContents")
        # print(body)
        # 제목
        title = content.h3.contents[0].strip()
        # print(title)

        # 본문
        sub = body.contents[0]
        con = ''
        while True:
            if sub is None:
                break
            if isinstance(sub, Tag):
                self.recursive_content(con, sub)
            elif isinstance(sub, NavigableString) and not isinstance(sub, Comment) and len(sub.string.strip()) > 0:
                con += sub.string.strip() + '\r\n'
            sub = sub.next_sibling
        return title, con

    def recursive_content(self, con, tag):
        for cont in tag.contents:
            if isinstance(cont, NavigableString) and not isinstance(cont, Comment) and len(cont.string.strip()) > 0:
                con += cont.string.strip() + '\r\n'
                return
            elif cont.name != 'a' and isinstance(cont, Tag):
                self.recursive_content(con, cont)

    '''
        # 2차 : <BR/>을 기준으로 이전 태그의 값을 가져오기(http://news.nate.com/view/20170320n43784?mid=n0301)
        if len(con.strip()) == 0:
            con = ''
            brs = body.find_all('br')
            for br in brs:
                br = br.previous_sibling
                if not isinstance(br, NavigableString) or len(br.string.strip()) == 0:
                    continue
                #print(br)
                con += br.string.strip() + '\r\n'

        # 3차 : <P> 태그의 값 가져오기
        if len(con.strip()) == 0:
            con = ''
            ps = body.find_all('p')
            for p in ps:
                if len(p.string.strip()) == 0:
                    continue
                #print(p)
                con += p.string.strip() + '\r\n'
    '''



    def crawl(self):
        def perdelta(start, end, delta):
            curr = start
            while curr < end:
                yield curr
                curr += delta

        base_url = "http://news.nate.com"
        # base_year = '2017'
        category = "eco"
        date = datetime.datetime.strptime(newsCrawlFromDate, "%Y-%m-%d").date()
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
                postNoList = soup.findAll("div", { "class" : "postNoList" })
                # print('classes :', postNoList.__len__())
                if postNoList.__len__() == 0:
                    for item in titlebody:
                        if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
                            continue
                        for li_item in item.find_all("li"):
                            try:
                                item_title = li_item.a.contents[0].strip()

                                if str(item_title).__contains__(keyword):
                                    print(item_title)
                                    item_link = base_url + li_item.a['href']
                                    item_source = li_item.span.contents[0].strip()
                                    article = {'title:': item_title,
                                               'link': item_link,
                                               'item_source': item_source}
                                    # print(article['item_link'])
                                    yield article
                            except:
                                continue

                else:
                    # print('기사 없음')
                    break


class NaverNews:
    def crawl(self):
        url = 'http://finance.naver.com/item/news_news.nhn?code=035720&page=1962'
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
        #        print(soup.prettify())
        tags = soup.find_all(name='td')
        idx = 0
        for tag in tags:
            if len(tag.contents) > 0 and (tag.contents[0].name == 'span' or idx > 0):
                sub_tag = tag.contents[0]
                idx = idx + 1
                if idx == 1:
                    print(sub_tag.contents[0])
                    print(str(sub_tag.contents[0]))
                    print(repr(sub_tag.contents[0]))
                    date = time.strptime(str(sub_tag.contents[0]).strip(), '%Y.%m.%d %H:%M')
            elif idx == 2:
                title = repr(sub_tag.contents[0]).strip()
            else:
                publisher = repr(sub_tag).strip()
                idx = 0
                print((date, publisher, title))


trainingSet = []
classList = []
testEntry = []
testArticleList = []

def Training():
    for article in article_list:
        # print(article)
        # title = article[0]
        # link = article[1]
        # newspaper = article[2]
        kkma = Kkma()

        try:
            content, issueDateTime = NateNews.get_content(article['link'])
            issueDateTime = pd.to_datetime(issueDateTime)
            # issueDate = time.strftime('%Y-%m-%d', issueDateTime)
            # issueTime = time.strftime('%H:%M:%S', issueDateTime)
            issueDate = issueDateTime.date()
            issueTime = issueDateTime.time()

            # 형태소 분석
            # wordList = kkma.pos(content)

            # [보통명사 동사 형용사 보조동사 명사추정범주] 필터링
            wordList = getWords(kkma.pos(content))

            wordList = list(wordList)
            # print(title)
            # print('wordList : ', wordList)
            # print(issueDateTime)
            # print(link)
            # print(newspaper)
            # print(issueDate)
            # print('wordList : ', wordList)

            baseDate = ''
            if issueTime > pd.to_datetime('15:30:00').time():
                # print('장 마감 이후')
                baseDate = stockDF[stockDF['날짜'] > issueDate].head(1)['날짜']
            else:
                # print('장 마감 이전')
                baseDate = stockDF[stockDF['날짜'] >= issueDate].head(1)['날짜']

            # print(type(baseDate))
            if issueDate > pd.to_datetime(testSetFromDate).date() or len(baseDate) == 0:
                # test set
                testEntry.append({'issueDateTime': issueDateTime, 'wordList': wordList})
            else:
                # trainning set
                baseDate = pd.Series(baseDate).values[0]
                # print('해당 일자 주식 확인 : ', baseDate)
                trainingSet.append({'issueDateTime': issueDateTime, 'wordList': wordList})
                # print(int(stockDF[stockDF['날짜'] == baseDate]['종가']))
                # print(int(stockDF[stockDF['날짜'] < baseDate].tail(1)['종가']))

                todayPrice = int(stockDF[stockDF['날짜'] == baseDate]['종가'])
                prevPrice = int(stockDF[stockDF['날짜'] < baseDate].tail(1)['종가'])
                if (todayPrice > prevPrice):
                    # print(baseDate, ' : up')
                    classList.append(1)
                else:
                    if (todayPrice < prevPrice):
                        # print(baseDate, ' : down')
                        classList.append(0)
                    else:
                        # print(baseDate, ' : hold')
                        classList.append(0)
        except:
            pass

def getWords(wordList):
    for word in wordList:
        if(len(word[0]) > 1 and tagList.__contains__(word[1])):
            yield word[0]

def Test():
    vocaList = nb.createVocabList(trainingSet)

    trainMat = []
    for postinDoc in trainingSet:
        trainMat.append(nb.setOfWords2Vec(vocaList, postinDoc['wordList']))

    output_path = 'output_' + str(datetime.datetime.today().date())
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

    # print('vocaList : ', vocaList)
    # print('trainMat : ', trainMat)
    # print('trainingSet : ', trainingSet)
    # print('testEntry : ', testEntry)
    # print('len(trainMat) : ', len(trainMat))
    # print('len(classList) : ', len(classList))
    # print('array(trainMat) : ', array(trainMat))
    # print('array(classList) : ', array(classList))
    p0V, p1V, pAb = nb.trainNB0(array(trainMat), array(classList))

    resultFileName = 'output_' + str(datetime.datetime.today().date()) + '.csv'
    f = open(resultFileName, 'w')
    cw = csv.writer(f)

    for entry in testEntry:
        thisDoc = array(nb.setOfWords2Vec(vocaList, entry['wordList']))
        result = nb.classifyNB(thisDoc, p0V, p1V, pAb)
        cw.writerow([entry['issueDateTime'], result])
        # print(entry['issueDateTime'], '기사 이후 주가는 ?\n', result)

    f.close()

stockDF = Stock().getStockData()
# print(stockDF)

keyword = '카카오'
newsCrawlFromDate = '2015-01-01'
testSetFromDate = '2017-01-01'
getPageCount = 300


news = NateNews()
article_list = news.crawl()
# print('article_list : ', article_list)
Training()

Test()
