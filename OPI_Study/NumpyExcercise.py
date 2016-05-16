#-*- coding:utf-8 -*-

import numpy as np

# 배열 만들기
a = np.array([0,1,2,3,4,5])
print(a)
print(a.ndim)
print(a.shape)


# 2차원(3 x 2) 매트릭스로 변형
b = a.reshape((3,2))
print(b)
print(b.ndim)
print(b.shape)


# 2행 1열 데이터 바꾸기
print(b[1][0])
b[1][0] = 77
print(b)
# b의 값뿐 아니라 a의 값도 바뀐다.
print(a)


# a와 독립적인 복사본 만들기
c = a.reshape((3,2)).copy()
print(c)
c[0][0] = -99
print(c)
# a의 원소는 바뀌지 않는다.
print(a)


# Numpy 배열의 장점은 연산자가 개별 원소에 전파된다는 것이다.
print(a*2)
print(a**2)
# vs 비교
print([1,2,3,4,5]*2)
# print([1,2,3,4,5]**2)     # 에러난다


# True/False
print(a>4)
# Filtering
print(a[a>4])



# 실행 시간 비교 : 1부터 1000까지 각각을 제곱한 후 총합을 구하고 10000번 반복
for i in range(10000):
    sum(x*x for x in range(1000))

import timeit
normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na = np.arange(1000)", number=10000)
goop_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np; na=np.arange(1000)", number=10000)

print("Normal Python : %f sec" %normal_py_sec)
print("Naive Numpy : %f sec" %naive_np_sec)
print("Good Numpy : %f sec" %goop_np_sec)

print("Normal Python : Good Numpy의 %f 배" %(normal_py_sec/goop_np_sec))
print("Naive Numpy : Good Numpy의 %f 배" %(naive_np_sec/goop_np_sec))



# 행렬의 원소 합 구하기
print(np.sum(c))
print(np.sum(c, axis=0))       #컬럼별 합계
print(np.sum(c, axis=1))       #행별 합계


# 전치행렬 구하기
print(c)
print(c.T)




# 브로드캐스팅(Broadcasting) : 크기가 다른 배열 간의 연산
#  우리는 x 행렬의 각 행에 v 벡터를 더해주고 그 결과를 y에 저장하고 싶다.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # empty_like 함수는 x 행렬과 같은 shape의 비어있는 배열을 만들어준다.

# 반복문을 이용해 x의 각 행에 v 벡터를 더하고 y에 저장하는 방법
for i in range(4):
    y[i, :] = x[i, :] + v



# numpy 브로드캐스팅은 실제로 v를 여러번 복사한 것을 만드는 것 없이 이 계산이 가능하다.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v
print(y)


'''
Numpy는 고성능의 다차원 배열과 이들 배열을 다루기 위한 기본 도구들을 제공한다.
SciPy 는 이것 위에 만들어지고, 넘파이 배열에 작동하는 많은 수의 함수를 제공하고, 과학적이고 공학적인 응용의 다른 타입들에 유용하다.
'''

import matplotlib.pyplot as plt

# 사인곡선에 해당하는 x와 y 좌표를 계산하자
x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)

# matplotlib를 사용해 점들을 표시하자
plt.plot(x, y)
plt.show()  # 그래픽 표현을 만들기 위해서는 plt.show() 함수를 꼭 불러줘야한다.



# 사인과 코싸인 곡선에 해당하는 x, y 좌표를 꼐산하자
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# matplotlib를 이용해 점들을 나타내자.
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()




# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# subplot의 모양이 높이는 2고 너비는 1로 설정하자.
# 그리고 첫번째 subplot을 활성화한다.
plt.subplot(2, 1, 1)

# 첫번째 plot을 만든다.
plt.plot(x, y_sin)
plt.title('Sine')

# 두번째 plot을 활성화하고, 두번째 plot을 만든다.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# 그림을 나타낸다.
plt.show()