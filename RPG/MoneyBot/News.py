#-*- coding:utf-8 -*-
import datetime
from bs4 import BeautifulSoup, NavigableString, Comment, Tag
import urllib
import pandas as pd

'''
기간별 기사
'''
def crawl(stockName):
    def perdelta(start, end, delta):
        curr = start
        while curr < end:
            yield curr
            curr += delta

    base_url = "http://news.nate.com"
    category = "eco"
    date = datetime.datetime.strptime('2018-01-01', "%Y-%m-%d").date()
    lastDate = datetime.date.today()

    getPageCount = 10

    article_cnt = 0
    article_list = list()

    # 기사 목록 추출
    for d in perdelta(date, lastDate, datetime.timedelta(days=1)):
        for i in range(1, getPageCount):
            target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + str(d).replace('-','') + "&page=" + repr(i)
            soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
            # print(soup)
            titlebody = soup.find_all("ul")

            postNoList = soup.findAll("div", {"class": "postNoList"})
            # print('classes :', postNoList.__len__())
            if postNoList.__len__() == 0:
                for item in titlebody:
                    if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
                        continue
                    for li_item in item.find_all("li"):
                        try:
                            item_title = li_item.a.contents[0].strip()

                            if str(item_title).__contains__(stockName):
                                item_link = base_url + li_item.a['href']
                                item_source = li_item.span.contents[0].strip()
                                article = {'title:': item_title,
                                           'link': item_link,
                                           'item_source': item_source}
                                # print(article['item_link'])
                                article_list.append(article)
                        except:
                            continue

            else:
                # print('기사 없음')
                break

    return article_list


'''
하루 기사
'''
def crawl(stockName, date):
    def perdelta(start, end, delta):
        curr = start
        while curr < end:
            yield curr
            curr += delta

    base_url = "http://news.nate.com"
    category = "eco"

    getPageCount = 300

    article_cnt = 0
    article_list = list()

    # 기사 목록 추출
    for d in perdelta(date+datetime.timedelta(days=-1), date, datetime.timedelta(days=1)):
        for i in range(1, getPageCount):
            target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + str(date).replace('-', '') + "&page=" + repr(i)
            soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
            titlebody = soup.find_all("ul")

            postNoList = soup.findAll("div", {"class": "postNoList"})
            # print('classes :', postNoList.__len__())
            if postNoList.__len__() == 0:
                for item in titlebody:
                    if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
                        continue
                    for li_item in item.find_all("li"):
                        try:
                            item_title = li_item.a.contents[0].strip()

                            if str(item_title).__contains__(stockName):
                                item_link = base_url + li_item.a['href']
                                item_source = li_item.span.contents[0].strip()
                                article = {'title': item_title,
                                           'link': item_link,
                                           'item_source': item_source}
                                # print(article['item_link'])
                                article_list.append(article)
                        except:
                            continue

            else:
                # print('기사 없음')
                break

    return article_list

def crawlByStockNameList(stockNameList, date):
    def perdelta(start, end, delta):
        curr = start
        while curr < end:
            yield curr
            curr += delta

    base_url = "http://news.nate.com"
    category = "eco"

    getPageCount = 300

    article_cnt = 0
    article_list = list()

    # 기사 목록 추출
    for d in perdelta(date+datetime.timedelta(days=-1), date, datetime.timedelta(days=1)):
        for i in range(1, getPageCount):
            target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + str(date).replace('-', '') + "&page=" + repr(i)
            soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
            titlebody = soup.find_all("ul")

            postNoList = soup.findAll("div", {"class": "postNoList"})
            # print('classes :', postNoList.__len__())
            if postNoList.__len__() == 0:
                for item in titlebody:
                    if (not (item.has_attr("class") and 'mduSubject' in item["class"])):
                        continue
                    for li_item in item.find_all("li"):
                        try:
                            item_title = li_item.a.contents[0].strip()

                            for item in stockNameList:
                                if item_title.__contains__(item):
                                    item_link = base_url + li_item.a['href']
                                    item_source = li_item.span.contents[0].strip()
                                    article = {'title': item_title,
                                               'link': item_link,
                                               'item_source': item_source}
                                    # print(article['item_link'])

                                    if article_list.__contains__(article):
                                        pass
                                    else:
                                        article_list.append(article)

                        except:
                            continue

            else:
                # print('기사 없음')
                break

    return [dict(t) for t in set([tuple(d.items()) for d in article_list])]

def get_content(url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
    # print(soup.prettify())
    content = soup.find(id="articleView")
    body = soup.find(id="realArtcContents")
    if body is None:
        return None, None

    # 제목
    # title = soup.find(id="articleSubecjt")
    # print(url)
    try:
        issueDatetime = pd.to_datetime(content.em.contents[0])
        # 본문
        # 1차 : 기본방법
        con = ""
        try:
            for child in body.children:
                if (not isinstance(child, NavigableString) or isinstance(child, Comment)) or child.string is None or len(child.string.strip()) == 0:
                    continue
                con += child.string.strip()
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
                        con += str
            except:
                pass

        return con, issueDatetime
    except:
        pass

def get_title(url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
    # print(soup.prettify())
    metas = soup.find_all('meta')

    for item in metas:
        if(item.has_attr('name') and 'nate:title' in item['name']):
            news_title = item['content']

        if (item.has_attr('name') and 'nate:site_name' in item['name']):
            item_source = item['content']

    return news_title, item_source


#  news_title, item_soruce update
# import RPG.MoneyBot.MySQL as sql
# query = " SELECT DISTINCT url FROM aibril_alu WHERE  news_title IS NULL OR news_title = 'None' "
# rtn = sql.selectStmt(query)
# for news in rtn:
#     print(news[0])
#     news_title, item_source = get_title(news[0])
#     print(news_title, item_source)
#     updateQuery = "update aibril_alu set news_title = '%s', item_source = '%s' where url = '%s' " % (str(news_title).replace("'", "''"), item_source, news[0])
#     sql.insertStmt(updateQuery)