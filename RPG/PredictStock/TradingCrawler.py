'''
Created on 2017. 5. 21.

@author: Administrator
'''
import requests 
import pandas as pd
from datetime import timedelta
from datetime import datetime
from bs4 import BeautifulSoup

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

#target code (current code = kakao)
target = ("035720" , 0 ,"카카오")

#input day
toDate = "2017-06-21"

#count data getting
dataCount = 250000

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

                datetimeList.append(dt)
                closePriceList.append(pClose)
                startPriceList.append(pStart)
                minPriceList.append(pMin)
                maxPriceList.append(pMax)
                amountList.append(amount)
        idx += 1
        
    if mode == "part" :
        if (code + str(shift))== (target[0] + str(target[1])):
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

 
#target 처리  


# data = GetPriceData(target, "part", None)
# for item in c_KTOP30:
#     data = GetPriceData(item, "part", data)
#
# data.to_csv("data_" +datetime.now().strftime("%Y%m%d%H%M%S")+ ".csv")



# target = ("000660" , 0 ,"하이닉스")
data = GetPriceData(target,"all")



print(target['datetime'])

# outFileName = "data/" + target[2] + "(" + target[0] + ")_" +datetime.now().strftime("%Y%m%d%H%M%S")+ ".csv"
# data.to_csv(outFileName)

