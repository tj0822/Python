#-*- coding:utf-8 -*-

'''
	· 제목 : 장대양봉
	· 매매 시점 : 다음날 종가
	· 목표 기간 : 1주일
	· 목표 수익률 : 5%
	· 목표 승률 : 80%
	· 알고리즘 상세
	1) 장대양봉 찾기 : 시가 > 종가(5%이상, 저가=시가 고가=종가)
	2) 하락신호가 오기 전까지 들고 있기
'''

import pandas as pd
import datetime

from os import listdir
from os.path import isfile, join

targetPeriod = 20
targetProfitRate = 1.05

stockDirectory = 'data/2017-10-30/'
stockFiles = (f for f in listdir(stockDirectory) if isfile(join(stockDirectory, f)))

portfolio = {'000660', '035720'}

for fileName in stockFiles:
    # if(portfolio.__contains__(fileName[:fileName.index('_')])):
        stockDF = pd.read_csv(stockDirectory + fileName).sort(['datetime'])

        successCnt = 0
        failCnt = 0
        totalProfit = 0

        fromStartDate = datetime.datetime.strptime('2010-01-01', "%Y-%m-%d").date()


        for i in range(1, len(stockDF)):
            if(datetime.datetime.strptime(stockDF[i:i + 1]['datetime'].values[0], "%Y-%m-%d").date() >= fromStartDate
               and int(stockDF[i:i+1]['close']) == int(stockDF[i:i+1]['high'])
               and int(stockDF[i:i+1]['open']) == int(stockDF[i:i+1]['low'])
               and int(stockDF[i:i+1]['open']) < int(stockDF[i-1:i]['close'] * (1+0.05))
               ):
                profit = 0
                buyPrice = int(stockDF[i:i + 1]['close'])
                buyDate = str(stockDF[i:i + 1]['datetime'])
                targetPrice = round(buyPrice * targetProfitRate, -2)
                # print('매수가 : ', buyPrice, ' 매수일자 : ', buyDate, '목표가 : ', targetPrice)

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
                if(totalProfit < 0.95):
                    profit = int(stockDF[j:j + 1]['close']) - buyPrice
                    totalProfit += profit
                    print('(실패) 매도가 : ', int(stockDF[j:j + 1]['close']), ' 매도일자 : ', stockDF[j:j + 1]['datetime'], ' 손실 : ', profit,' 누적 수익 : ', totalProfit)
                    failCnt += 1


        print(fileName.replace('.csv', ''), ' : ' '성공 : ', successCnt, ' 실패 : ', failCnt,' 누적 수익 : ', totalProfit)