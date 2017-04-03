#-*- coding:utf-8 -*-

import xlrd
import pandas as pd
import collections
import matplotlib.pyplot as plt

wb = xlrd.open_workbook('data/lotto_1to742.xlsx')
ws = wb.sheet_by_index(0)

ncol = ws.ncols
nrow = ws.nrows

l = list()
cols = list()
for i in range(0, nrow):
    # print(ws.row_values(i))
    if i==0:
        cols.append(ws.row_values(i))
    else :
        l.append(ws.row_values(i))

# print(cols[0])
df = pd.DataFrame(l, columns=cols[0])

unpacklist = list()

unpacklist.append(tuple(df.N1))
unpacklist.append(tuple(df.N2))
unpacklist.append(tuple(df.N3))
unpacklist.append(tuple(df.N4))
unpacklist.append(tuple(df.N5))
unpacklist.append(tuple(df.N6))

print(tuple(unpacklist[0]))
counter = collections.Counter(tuple(unpacklist[0]))

print(counter.most_common(6))
