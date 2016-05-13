#-*- coding:utf-8 -*-
import nlib

A = nlib.Matrix([[1, 2, 2], [4, 4, 2], [4, 6, 5]])
B = nlib.Matrix([[3], [6], [10]])

x = (1/A)*B
print('x : ' + str(x))
