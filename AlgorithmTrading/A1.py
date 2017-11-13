#-*- coding:utf-8 -*-

'''
	· 제목 : 갭하락 양봉
	· 매매 시점 : 장 마감 직전 종가
	· 목표 기간 : 2일
	· 목표 수익률 : 2%
	· 목표 승률 : 80%
	· 알고리즘 상세
	1) 갭하락 양봉 패턴 찾기 : 당일 종가는 전날 저가보다 높지 않아야 함
	2) 당일 장 마감 직전에 종가로 매수
	3) 다음날 장 초반에 매수가의 2%수익에 매도 시도
	4) 2일후에 매도되지 않으면 무조건 시가 매도
'''

import pandas as pd
import datetime
import csv
import math

from os import listdir
from os.path import isfile, join

# seedmoney = 10000000
targetPeriod = 3
# targetProfit = 0.01
# targetProfitRate = 1.0033 + targetProfit
#
seedmoney = 10000000
stockDirectory = 'data/2017-11-04/'
portfolio = {'008560'}
#
# fromSimulYear = '2015'
# toSimulYear = '2016'
# fromSimulDate = datetime.datetime.strptime(fromSimulYear + '-01-01', "%Y-%m-%d").date()
# toSimulDate = datetime.datetime.strptime(toSimulYear + '-01-01', "%Y-%m-%d").date()

def Simulator(fromSimulYear=2010, toSimulYear = 2011, targetProfit = 0.01):
    targetProfitRate = 1.0033 + targetProfit
    stockFiles = (f for f in listdir(stockDirectory) if isfile(join(stockDirectory, f)))
    fromSimulDate = datetime.datetime.strptime(str(fromSimulYear) + '-01-01', "%Y-%m-%d").date()
    toSimulDate = datetime.datetime.strptime((str(toSimulYear) + '-01-01'), "%Y-%m-%d").date()



    for fileName in stockFiles:
        # if(portfolio.__contains__(fileName[:fileName.index('_')])):
            stockDF = pd.read_csv(stockDirectory + fileName).sort(['datetime'])

            successCnt = 0
            failCnt = 0
            totalProfit = 0
            stockCnt = 0
            cash = seedmoney
            stockValue = 0

            bInit = True
            initPrice = 0  # 연초 최초 구입가격
            initStockCnt = 0

            tempBuyPrice = 0
            tempCnt = 1
            tempTargetPrice = 0

            for i in range(2, len(stockDF)):
                before2dayDatetime = datetime.datetime.strptime(stockDF[i - 2:i - 1]['datetime'].values[0], "%Y-%m-%d").date()
                before2dayOpen = int(stockDF[i - 2:i-1]['open'])
                before2dayClose = int(stockDF[i - 2:i-1]['close'])
                before2dayLow = int(stockDF[i - 2:i-1]['low'])
                before2dayHigh = int(stockDF[i - 2:i-1]['high'])
                yesterdayVolume = int(stockDF[i - 2:i-1]['volume'])

                yesterdayDatetime = datetime.datetime.strptime(stockDF[i - 1:i]['datetime'].values[0], "%Y-%m-%d").date()
                yesterdayOpen = int(stockDF[i-1:i]['open'])
                yesterdayClose = int(stockDF[i-1:i]['close'])
                yesterdayLow = int(stockDF[i-1:i]['low'])
                yesterdayHigh = int(stockDF[i-1:i]['high'])
                yesterdayVolume = int(stockDF[i-1:i]['volume'])

                todayDatetime = datetime.datetime.strptime(stockDF[i:i + 1]['datetime'].values[0], "%Y-%m-%d").date()
                todayOpen = int(stockDF[i:i+1]['open'])
                todayClose = int(stockDF[i:i+1]['close'])
                todayLow = int(stockDF[i:i+1]['low'])
                todayHigh = int(stockDF[i:i+1]['high'])
                todayVolume = int(stockDF[i:i+1]['volume'])

                if todayDatetime >= fromSimulDate and (yesterdayVolume * todayVolume) > 0:
                    if bInit:
                        initPrice = todayClose      # 연초 최초 구입가격
                        initStockCnt = int(cash / todayClose)
                        # print(todayDatetime, ' ', initPrice, ' ', initStockCnt)
                        bInit = False
                    else :
                        if todayDatetime <= toSimulDate:
                            if stockCnt == 0:
                                if(before2dayClose >= before2dayOpen * 1.05
                                    and yesterdayClose < yesterdayOpen
                                    and yesterdayClose > before2dayOpen
                                    and todayOpen < todayClose
                                    and todayOpen < yesterdayOpen
                                    and todayClose < yesterdayClose
                                   ):
                                # if (todayOpen < yesterdayClose
                                #     and todayOpen < yesterdayOpen
                                #     and todayOpen < todayClose
                                #     and todayClose > yesterdayOpen
                                #     and todayClose > yesterdayClose
                                #     ):
                                    tempBuyPrice = todayClose
                                    if todayClose < 10000:
                                        tempTargetPrice = math.ceil(tempBuyPrice * targetProfitRate / 10) * 10
                                    elif todayClose >= 10000 and todayClose < 100000:
                                        tempTargetPrice = math.ceil(tempBuyPrice * targetProfitRate / 100) * 100
                                    elif todayClose >= 100000:
                                        tempTargetPrice = math.ceil(tempBuyPrice * targetProfitRate / 1000) * 1000
                                    buyCnt = int(cash / todayClose)
                                    stockCnt = stockCnt + buyCnt

                                    cash = cash - (todayClose * buyCnt)
                                    stockValue = todayClose * stockCnt
                                    # print('현금 : ', cash, ' 주식가치 : ', stockValue, ' total value : ', cash+stockValue)
                                    print('매수일자 : ',  todayDatetime, ' 매수가격 : ', tempBuyPrice, ' 목표가격 : ', tempTargetPrice)
                                else:
                                    continue
                            else:
                                if (todayHigh >= tempTargetPrice):
                                    sellPrice = tempTargetPrice
                                    print('(성공) 매수가 : ', tempBuyPrice, '매도가 : ', sellPrice, '수량 : ', stockCnt,' 매도일자 : ', tempCnt, '거래일', ' 차액 : ', (sellPrice - tempBuyPrice))
                                    successCnt = successCnt + 1
                                    cash = cash + sellPrice * stockCnt
                                    stockCnt = 0
                                else:
                                    if(tempCnt == targetPeriod):
                                        sellPrice = todayClose
                                        print('(실패) 매수가 : ', tempBuyPrice, '매도가 : ', sellPrice, '수량 : ', stockCnt, ' 매도일자 : ', todayDatetime, ' 차액 : ', (sellPrice-tempBuyPrice))
                                        failCnt = failCnt + 1
                                        cash = cash + todayClose * stockCnt
                                        stockCnt = 0
                                        tempCnt = 0
                                    else:
                                        tempCnt = tempCnt + 1
                                        continue
                        else:
                            totalValue = cash + todayClose * stockCnt
                            #print(fileName, ' - 성공 : ', successCnt, ' 실패 : ', failCnt, '정산일 : ', todayDatetime, ' 현금 : ', cash, ' 수량 : ', stockCnt,' 종가 : ', todayClose, ' 총자산 : ', totalValue, ' 수익률 : ',(totalValue - seedmoney) / seedmoney * 100)
                            # print('연초 구매수량 : ', initStockCnt)

                            if successCnt+failCnt > 0:
                                wr.writerow([fileName.split('_')[0], fileName.split('_')[1].split('.')[0], fromSimulYear, str(successCnt+failCnt), str(targetProfit), (totalValue - seedmoney) / seedmoney * 100, (todayClose*initStockCnt - seedmoney) / seedmoney * 100])
                                print(fileName.split('_')[0], ' ', fileName.split('_')[1].split('.')[0], ' 투자년도 : ', fromSimulYear, '거래 횟수 : ', successCnt + failCnt, '목표수익률 : ', str(targetProfit), ' 수익률 : ', (totalValue - seedmoney) / seedmoney * 100, ' vs 연초 대비 수익률 : ', (todayClose * initStockCnt - seedmoney) / seedmoney * 100)

                            break;


f = open('output_' + str(datetime.datetime.now())[:10] + '.csv', 'w', newline='')
wr = csv.writer(f)

for year in range(2010, 2017, 1):
    for targetProfit in range(1, 6, 1):
        Simulator(fromSimulYear=year, toSimulYear=year+1, targetProfit=targetProfit/100)
f
f.close()

'''       
            if(datetime.datetime.strptime(stockDF[i:i + 1]['datetime'].values[0], "%Y-%m-%d").date() >= fromStartDate
               and int(stockDF[i:i+1]['close']) > int(stockDF[i:i+1]['open'])
               and int(stockDF[i:i+1]['open']) > int(stockDF[i:i+1]['low'])
               and int(stockDF[i:i+1]['high']) < int(stockDF[i-1:i]['low'])
               ):
                profit = 0
                buyPrice = int(stockDF[i:i + 1]['close'])
                buyDate = str(stockDF[i:i + 1]['datetime'])
                targetPrice = round(buyPrice * targetProfitRate, -2)
                print('매수가 : ', buyPrice, ' 매수일자 : ', buyDate, '목표가 : ', targetPrice)

                for j in range(i+1, i+1+targetPeriod):
                    # print(stockDF[j:j+1]['datetime'].values[0])
                    # print(stockDF[j:j + 1]['high'].values[0])
                    highPrice = int(stockDF[j:j+1]['high'])
                    if(targetPrice < highPrice):
                        sellDate = str(stockDF[j:j+1]['datetime'])
                        profit = targetPrice-buyPrice
                        totalProfit += profit
                        print('(성공) 매도가 : ', targetPrice, ' 매도일자 : ', sellDate, ' 수익 : ', profit, ' 누적 수익 : ', totalProfit)
                        successCnt += 1
                        break
                else:
                    profit = int(stockDF[j:j + 1]['close']) - buyPrice
                    totalProfit += profit
                    print('(실패) 매도가 : ', int(stockDF[j:j + 1]['close']), ' 매도일자 : ', stockDF[j:j + 1]['datetime'], ' 손실 : ', profit,' 누적 수익 : ', totalProfit)
                    failCnt += 1
'''

        # print(fileName.replace('.csv', ''), ' : ' '성공 : ', successCnt, ' 실패 : ', failCnt,' 누적 수익 : ', totalProfit)