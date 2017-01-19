#-*- coding:utf-8 -*-

g = 10

def fn():
    global g
    g = 100
    print("g = ", g)

fn()
print("g = ", g)

print("hello python...")

import  sys
