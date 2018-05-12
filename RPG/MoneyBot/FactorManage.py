#-*- coding:utf-8 -*-


# 은퇴자금 구하기
'''
은퇴자금 = (M*12) * (1+i)^n / (R-i)
M : 은퇴 후 월 필요 지출액
R : 은퇴후 기대 CAGR(연복리 수익률)
i : 물가 상승률 2~3%
n : 은퇴까지 남은 연수(남은 근속 년수
'''

def CalcRetirement(M=5000000, R=0.09, i=0.04 , n=10):
    result = (M*12) * pow(1+i, n) / (R-i)
    print('필요한 은퇴 자금은? 약 ', format(round(int(result), -4), ','), '원',  sep='')


CalcRetirement()