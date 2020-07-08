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
import MySQL as sql


def GetPriceData(item, mode = "part", data = None):
    # print(item)
    code = item[0]
    shift = item[1]
    name = item[2]
    # header = code + "_" + str(shift)
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
        # print(soup.find('td', class_='on').find('a').text)
        if soup.find('td', class_='on').find('a').text != str(idx):
            break

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

                if(datetimeList.__contains__(dt) or dt == ""):
                    bBool = False
                    break
                else:
                    # datetimeList.append(dt)
                    # closePriceList.append(pClose)
                    # startPriceList.append(pStart)
                    # minPriceList.append(pMin)
                    # maxPriceList.append(pMax)
                    # amountList.append(amount)

                    selectQuery = "select count(*) from stock_history where date = '%s' and stock_code = '%s' " % (dt, code)
                    result = sql.selectStmt(selectQuery)
                    # print(int(result[0][0]))
                    if int(result[0][0]) == 0:
                        # 투자정보
                        # totalCnt = []  # 상장주식수
                        # forignerHaveLimit = []  # 외국인한도보유주식수
                        # forignerHaveCnt = []  # 외국인보유주식수
                        # max52week = []  # 52주 최고
                        # min52week = []  # 52주 최저
                        # per = []
                        # eps = []
                        # per_eps_date = []
                        # estimate_per = []  # 추정 PER
                        # estimate_eps = []  # 추정 EPS
                        # pbr = []
                        # bps = []
                        # pbr_bps_date = []
                        # dvr = []  # 배당수익

                        url = "https://finance.naver.com/item/main.nhn?code=" + code
                        source_code = requests.get(url)
                        if source_code is None:
                            break
                        soup = BeautifulSoup(source_code.text, "lxml")

                        # print(soup.find(id='tab_con1').find_all('em'))
                        totalCnt = float(soup.find(id='tab_con1').find_all('em')[2].text.replace(',', '').replace('N/A', '0'))
                        forignerHaveLimit = float(soup.find(id='tab_con1').find_all('em')[5].text.replace(',', '').replace('N/A', '0'))
                        forignerHaveCnt = float(soup.find(id='tab_con1').find_all('em')[6].text.replace(',', '').replace('N/A', '0'))
                        max52week = float(soup.find(id='tab_con1').find_all('em')[10].text.replace(',', '').replace('N/A', '0'))
                        min52week = float(soup.find(id='tab_con1').find_all('em')[11].text.replace(',', '').replace('N/A', '0'))
                        per = float(soup.find(id='tab_con1').find_all('em')[12].text.replace(',', '').replace('N/A', '0'))
                        eps = float(soup.find(id='tab_con1').find_all('em')[13].text.replace(',', '').replace('N/A', '0'))
                        per_eps_date = soup.find(id='tab_con1').find_all('span', class_='date')[0].text.replace('(','').replace(')','')
                        estimate_per = float(soup.find(id='tab_con1').find_all('em')[14].text.replace(',', '').replace('N/A', '0'))
                        estimate_eps = float(soup.find(id='tab_con1').find_all('em')[15].text.replace(',', '').replace('N/A', '0'))
                        pbr = float(soup.find(id='tab_con1').find_all('em')[16].text.replace(',', '').replace('N/A', '0'))
                        bps = float(soup.find(id='tab_con1').find_all('em')[17].text.replace(',', '').replace('N/A', '0'))
                        pbr_bps_date = soup.find(id='tab_con1').find_all('span', class_='date')[1].text.replace('(','').replace(')','')
                        dvr = float(soup.find(id='tab_con1').find_all('em')[18].text.replace(',', '').replace('N/A', '0'))

                        insertQuery = "insert into stock_history(date, stock_code, open_price, close_price, min_price, max_price, amount, timestamp, total_cnt, forignerHaveLimit, forignerHaveCnt, max52week, min52week, per, eps, per_eps_date, estimate_per, estimate_eps, pbr, bps, pbr_bps_date, dvr) VALUES ('%s', '%s', %d, %d, %d, %d, %d, NOW(), %d, %d, %d, %d, %d, %0.2f, %d, '%s', %0.2f, %d, %0.2f, %d, '%s', %0.2f ) " % (dt, code, pStart, pClose, pMin, pMax, amount, totalCnt, forignerHaveLimit, forignerHaveCnt, max52week, min52week, per, eps, per_eps_date, estimate_per, estimate_eps, pbr, bps, pbr_bps_date, dvr)
                        print(insertQuery)
                        sql.insertStmt(query=insertQuery)
                    else:
                        bBool = False
                        break
        idx += 1
'''        
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
'''



stockDict = stock.GetKospi200()
# stockDict = {'005930':'삼성전자'}

crawlDate = str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day)
print(crawlDate)
directory = 'data/' + crawlDate

for key in stockDict.keys():
    print(key, ':', stockDict[key])
    target = (key, 0, stockDict[key])
    # if eval('+'.join(key)) % 2 == 1:
    data = GetPriceData(target, "all")

    # if not os.path.exists(directory):
    #     os.makedirs(directory)
    #
    # outFileName = 'data/' + stockDict[key] + '.csv'
    # data.to_csv(outFileName)

# data = GetPriceData(target,"all")
#
#
# l = list(data.index.get_values())
#
#
# # outFileName = "data/" + target[2] + "(" + target[0] + ")_" +datetime.now().strftime("%Y%m%d%H%M%S")+ ".csv"
#
# crawlDate = str(datetime.date.today())
#
# outFileName = 'data/' + target[2] + '_' + str(min(l))[0:10].replace('-', '') + '~' + str(max(l))[0:10].replace('-', '') + '.csv'
# data.to_csv(outFileName)

