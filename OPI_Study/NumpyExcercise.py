#-*- coding:utf-8 -*-

import numpy as np

a = np.array([0,1,2,3,4,5])

print(a)
print(a.ndim)
print(a.shape)


b = a.reshape((3,2))
print(b)
print(b.ndim)
print(b.shape)

print(b[1][0])
b[1][0] = 77
print(b)
print(a)


c = a.reshape((3,2)).copy()
print(c)
c[0][0] = -99

print(c)
print(a)



print(a*2)
print(a**2)

print([1,2,3,4,5]*2)
# print([1,2,3,4,5]**2)


print(a>4)
print(a[a>4])



# 실행 시간 비교 : 1부터 1000까지 각각을 제곱한 후 총합을 구하고 10000번 반복
import timeit
normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na = np.arange(1000)", number=10000)
goop_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np; na=np.arange(1000)", number=10000)

print("Normal Python : %f sec" %normal_py_sec)
print("Naive Numpy : %f sec" %naive_np_sec)
print("Good Numpy : %f sec" %goop_np_sec)


