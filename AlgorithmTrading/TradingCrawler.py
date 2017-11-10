'''
Created on 2017. 5. 21.

@author: Administrator
'''
import requests 
import pandas as pd
from datetime import timedelta
from datetime import datetime
from bs4 import BeautifulSoup
import AlgorithmTrading.Stock as stock
import os

#ktop 30 code : name
c_KTOP30 = [
 ("000720" , 1 ,"현대건설"     )
,("000720" , 2 ,"현대건설"     )
,("000720" , 3 ,"현대건설"     )
,("032830" , 1 ,"삼성생명"     )
,("055550" , 1 ,"신한지주"     )
,("105560" , 1 ,"KB금융"       )
,("000810" , 1 ,"삼성화재"     )
,("035420" , 1 ,"Naver"        )
,("096770" , 1 ,"SK이노베이션" )
,("000270" , 1 ,"기아차"       )
,("005380" , 1 ,"현대차"       )
,("009540" , 1 ,"현대중공업"   )
,("012330" , 1 ,"현대모비스"   )
,("086280" , 1 ,"현대글로비스" )
,("028260" , 1 ,"삼성물산"     )
,("139480" , 1 ,"이마트"       )
,("000100" , 1 ,"유한양행"     )
,("035720" , 2 ,"카카오"       )
,("000660" , 1 ,"SK하이닉스"   )
,("005930" , 1 ,"삼성전자"     )
,("006400" , 1 ,"삼성SDI"      )
,("009150" , 1 ,"삼성전기"     )
,("034220" , 1 ,"LG디스플레이" )
,("066570" , 1 ,"LG전자"       )
,("068270" , 1 ,"셀트리온"     )
,("004020" , 1 ,"현대제철"     )
,("005490" , 1 ,"POSCO"        )
,("017670" , 1 ,"SK텔레콤"     )
,("011170" , 1 ,"롯데케미칼"   )
,("051910" , 1 ,"LG화학"       )
,("090430" , 1 ,"아모레퍼시픽" )
,("161390" , 1 ,"한국타이어"   )
]

favoriteStocks = {'KOSPI'}
#target code (current code = kakao)
# target = ("000660" , 0 ,"SK하이닉스")

toDate = '2017-09-21'

def GetPriceData(item, mode = "part", data = None):
    code = item[0]
    shift = item[1]
    name = item[2]
    header = code + "_" + str(shift)
    url = "http://finance.naver.com/item/sise_day.nhn?code=" + code

    page = "&page="
    idx = 1
    datetimeList = []
    closePriceList = []
    startPriceList = []
    minPriceList = []
    maxPriceList = []
    amountList = []
    bBool = True
    while bBool:
        fullAddr = url + page + str(idx)
        # print(fullAddr)
        source_code = requests.get(fullAddr)
        if source_code is None:
            break
        soup = BeautifulSoup(source_code.text,"lxml")
        # print(idx)
        # print(soup.find('td', class_='pgRR').find('a'))
        for tr in filter(lambda x:x.get("onmouseout") is not None, soup.find_all("tr")):

            if tr.find("span",class_ = "tah p10 gray03") is None:
                # 가격데이터가 없으면 False로 빠져나옴
                bBool = False

            else:
                tDate = tr.find("span",class_ = "tah p10 gray03").text
                cPrice = tr.find_all("span",class_ = "tah p11")
                sIdx = 1

                if len(cPrice) != 5 :
                    sIdx = 2

                dt = tDate.replace("." ,"-")
                pClose = float(cPrice[0].text.replace("," ,""))
                pStart = float(cPrice[sIdx].text.replace("," ,""))
                sIdx += 1
                pMax   = float(cPrice[sIdx].text.replace("," ,""))
                sIdx += 1
                pMin   = float(cPrice[sIdx].text.replace("," ,""))
                sIdx += 1
                amount = float(cPrice[sIdx].text.replace("," ,""))

                if(datetimeList.__contains__(dt)):
                    bBool = False
                    break
                else:
                    datetimeList.append(dt)
                    closePriceList.append(pClose)
                    startPriceList.append(pStart)
                    minPriceList.append(pMin)
                    maxPriceList.append(pMax)
                    amountList.append(amount)
        idx += 1
        
    if mode == "part" :
        if (code + str(shift))== (item[0] + str(item[1])):
            if toDate in datetimeList :
                idx = datetimeList.index(toDate)
                del datetimeList[:idx+1]
                del closePriceList[:idx+1]
            datetimeList.insert(0,toDate)
            closePriceList.insert(0,0)
            df = pd.DataFrame({"datetime" : datetimeList,"sum":closePriceList})
            df["datetime"] = df.datetime.map(lambda x: pd.to_datetime(x))      
            df = df.set_index("datetime")
            return df
        else :
            if toDate in datetimeList :
                idx = datetimeList.index(toDate)
                del datetimeList[:idx+1]
                del closePriceList[:idx+1]
            datetimeList.insert(0,toDate)
            closePriceList.insert(0,0)
            df = pd.DataFrame({"datetime" : datetimeList,header:closePriceList})
            df["datetime"] = df.datetime.map(lambda x: pd.to_datetime(x)).shift(shift)
            df = df.set_index("datetime")
            
            return pd.merge(data, df, how="left", left_index = True, right_index=True)
    elif mode == "all" :
        df = pd.DataFrame({"datetime" : datetimeList,"close":closePriceList,"open":startPriceList,"low":minPriceList,"high":maxPriceList,"volume":amountList})
        df["datetime"] = df.datetime.map(lambda x: pd.to_datetime(x))      
        df = df.set_index("datetime")
        return df


def GetKospiData(mode="all"):
    code = 'KOSPI'
    name = 'KOSPI'
    url = "http://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&"

    page = "&page="
    idx = 1

    # 마지막 페이지 찾기
    base_url = url + page + str(idx)
    # print(base_url)
    source_code = requests.get(base_url)

    soup = BeautifulSoup(source_code.text, "lxml")

    for item in soup.find_all('td'):
        if item.has_attr('class') and 'pgRR' in item['class']:
            # print(item.a['href'])
            lastPageNum = int(str(item.a['href']).replace('/sise/sise_index_day.nhn?code=KOSPI&&page=', ''))

    # print(lastPageNum)
    datetimeList = []
    numberList = []
    rate_down = []
    totalVolume = []
    totalPrice = []

    bBool = True
    while bBool:
        print(idx)
        fullAddr = url + page + str(idx)
        # print(fullAddr)
        source_code = requests.get(fullAddr)
        if source_code is None:
            break
        soup = BeautifulSoup(source_code.text, "lxml")
        # print(idx)
        # print(soup.find('td', class_='pgRR').find('a'))
        # print(soup)

        postNoList = soup.find_all('td')
        # print(postNoList)
        # 종목코드와 종목명 담기
        for item in postNoList:
            # 날짜
            if item.has_attr('class') and 'date' in item['class']:
                # print('날짜 : ', item.text.strip())
                # print(item.text.strip())
                if item.text.strip() == '':
                    break
                else:
                    datetimeList.append(item.text.strip())

            if item.has_attr('class') and 'number_1' in item['class']:
                # 거래량(천주)
                if item.has_attr('style') and 'padding-right:40px;' in item['style']:
                    # print('거래량 : ', item.text.strip())
                    totalVolume.append((item.text.replace(',', '').strip()))

                # 거래대금(백만)
                elif item.has_attr('style') and 'padding-right:30px;' in item['style']:
                    # print('거래대금 : ', item.text.strip())
                    totalPrice.append((item.text.replace(',', '').strip()))

                # 체결가
                else:
                    if item.find("span", class_="tah p11 nv01") == None and item.find("span", class_="tah p11 red01") == None\
                            and item.find("span", class_="tah p11 gray01") == None:
                        # print('체결가 : ', item.text.strip())
                        numberList.append((item.text.replace(',', '').strip()))
                    else:
                        # 등락률
                        # print('등락률 : ', item.text.strip())
                        rate_down.append((item.text.replace('%', '').strip()))

        idx += 1
        if idx > lastPageNum:
            bBool = False
            break;

    if mode == "all":
        df = pd.DataFrame(
            {"datetime": datetimeList, "number": numberList, "rate_down": rate_down, "totalVolume": totalVolume, "totalPrice": totalPrice})
        df["datetime"] = df.datetime.map(lambda x: pd.to_datetime(x))
        df = df.set_index("datetime")
        print(df)
        return df

# stockDict = stock.GetKospi200()
# stockDict['KOSPI'] = 'KOSPI'    # 코스피 강제 추가

crawlDate = str(datetime.now())[:10]
directory = 'data/' + crawlDate

'''
for key in stockDict.keys():
    if favoriteStocks.__contains__(key):
    #     print(key, ' : ', stockDict[key])
        data = GetPriceData((key, 0 ,stockDict[key]),"all")

        if not os.path.exists(directory):
            os.makedirs(directory)

        outFileName = directory + '/' + key + '_' + stockDict[key] + '.csv'
        data.to_csv(outFileName)
'''

kospi = GetKospiData('all')
if not os.path.exists(directory):
    os.makedirs(directory)

    outFileName = directory + '/' + 'KOSPI' + '_' + crawlDate + '.csv'
    kospi.to_csv(outFileName)

# print(kospi)

