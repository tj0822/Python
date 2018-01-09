'''
{
"url" : "https://gateway.aibril-watson.kr/natural-language-understanding/api",
"username" : "7457e1d2-26a8-4b82-8f4d-782ad438ac10",
"password" : "ZSZ5Wmt8zRUA"
}
'''
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
import datetime
from bs4 import BeautifulSoup, NavigableString, Comment, Tag
import urllib.request


class News:

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

        getPageCount = 300

        article_cnt = 0
        article_list = list()

        # 기사 목록 추출
        for d in perdelta(date, lastDate, datetime.timedelta(days=1)):
            for i in range(1, getPageCount):
                target_url = base_url + "/recent?cate=" + category + "&mid=n0301&type=t&date=" + str(d).replace('-', '') + "&page=" + repr(i)
                soup = BeautifulSoup(urllib.request.urlopen(target_url).read(), "lxml")
                # print(soup)
                titlebody = soup.find_all("ul")

                postNoList = soup.findAll("div", { "class" : "postNoList" })
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
                    # con += child.string.strip() + '\r\n'
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
                            # print(str)
                            # con += str + '\r\n'
                            con += str
                except:
                    pass

            return con, issueDatetime
        except:
            pass

class NLU:
    def response(contentText='', targets=None):
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            url='https://gateway.aibril-watson.kr/natural-language-understanding/api',
            username='7457e1d2-26a8-4b82-8f4d-782ad438ac10',
            password='ZSZ5Wmt8zRUA',
            version='2017-02-27')

        return natural_language_understanding.analyze(text=contentText, features=Features(sentiment=SentimentOptions(targets=[targets])))


stockList = {'카카오'}

for stockName in stockList:
    print(stockName)
    stockNewsList = News.crawl(stockName=stockName)

    for news in stockNewsList:
        contentText, issueDatetime = News.get_content(news['link'])
        if contentText.__contains__(stockName):
            print(issueDatetime)
            response = NLU.response(contentText=contentText,targets=stockName)
            print(response['sentiment']['targets'][0]['score'])
            print(response['sentiment']['document']['score'])


        # response = natural_language_understanding.analyze(
        # url='http://news.naver.com/main/list.nhn?mode=LS2D&sid2=258&sid1=101&mid=shm&date=20180108&page=1',
        # features=Features(
        # sentiment=SentimentOptions(
        # targets=['카카오'])))


# print(json.dumps(NLU.response, indent=2))


