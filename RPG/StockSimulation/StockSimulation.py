#-*- coding:utf-8 -*-

import csv

stockData = open("data/PRICE_181710(NHN엔터테인먼트).csv", 'r')
reader = csv.reader(stockData)
stockList = list(reader)


# 초기값 셋팅
stock = 0
seedmoney = 10000000
totalValue = 0
stock = 0
sellUnit = 1

# 매매 기준
profit = 0.05 # 총수익률이 5%이상이면 매도
loss = 0.05 # 총손해율이 5%이상이면 매도

#전날종가 대비 떨어진 당일 시가 금액 비율 기준(1%이상 떨어졌으면 매수)
downrate = 0.01
stockList.sort(reverse=False)

def buy():
    print("매수")
    global stock
    stock += sellUnit

def sell():
    print("매도")

for i in range(0, stockList.__len__()-1):
    if i == 0:
        continue
    else:
        if(stockList[i][2] < stockList[i-1][1]):
            buy();
        else:
            print("대기")

    print(stock)
