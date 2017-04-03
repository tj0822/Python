#-*- coding:utf-8 -*-

import scipy as sp
data = sp.genfromtxt('data/web_traffic.tsv', delimiter='\t')


# 데이터 읽기
print(data[:10])
# print(data.shape)


# 데이터 정리와 전처리
x = data[:,0]
y = data[:,1]

print(x)
print(y)
print(sp.sum(sp.isnan(y)))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
