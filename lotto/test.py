#-*- coding:utf-8 -*-

import xlrd
import pandas as pd

wb = xlrd.open_workbook('data/lotto_1to742.xlsx')
ws = wb.sheet_by_index(0)

ncol = ws.ncols
nrow = ws.nrows

l = list()

for i in range(0, nrow):
    # print(ws.row_values(i))
    l.append(ws.row_values(i))


df = pd.DataFrame(l)

print(df[12][0])

