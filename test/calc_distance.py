#-*- coding:utf-8 -*-

import math

def calcDistance(lst1, lst2):
    for idx in range(0,len(lst1)):
        d = (int(lst1[idx]) - int(lst2[idx])) ** 2
    print('d = ', math.sqrt(d))

