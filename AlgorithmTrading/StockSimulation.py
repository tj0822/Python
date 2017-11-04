#-*- coding:utf-8 -*-
import pandas as pd
import csv
from os import listdir
from os.path import isfile, join

'''
1. 시뮬레이션 기초 데이터 설정하기
    1) 초기 자산 : seedmoney
    2) 손절 기준 : lowerRate
    3) 수익 목표 : upperRate
'''
seedmoney = 10000000
upperRate = 0.1
lowerRate = -0.1

'''
2. 시뮬레이션할 주식 데이터 가져오기
'''
stockDirectory = 'data/2017-10-30/'
stockFiles = (f for f in listdir(stockDirectory) if isfile(join(stockDirectory, f)))

portfolio = {'000660', '035720'}

'''
3. 적용할 알고리즘 불러오기
'''

'''
4. 불러온 알고리즘으로 거래하기
'''