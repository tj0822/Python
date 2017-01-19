# -*- coding: utf-8 -*-
'''
Created on 2015. 9. 4.

@author: TaijinKim
'''
import kNN
from imp import reload

#2.1 k-최근접 이웃 알고리즘
# group, labels = kNN.createDataSet()
# print(group)
# print(labels)
# print(kNN.classify0([0, 0], group, labels, 3))


#2.2 Numpy 구문 분석 코드에 텍스트 기록하기
# reload(kNN)
# datingDataMat, datingLabels = kNN.file2matrix('../data/datingTestSet2.txt')
# print(datingDataMat)
# print(datingLabels)

#2.2.2 분석: 매스플롯라이브러리로 scatte 플롯 생성하기
# import matplotlib
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# plt.show()
#
# from numpy import array
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels).astype(float), 15.0*array(datingLabels).astype(float))
# plt.show()


#2.3 데이터 정규화하기 코드
# reload(kNN)
# norMat, ranges, minVals = kNN.autoNorm(datingDataMat)
# print(norMat)
# print(ranges)
# print(minVals)


# 2.4 데이트하기 사이트를 위한 분류기 검사 코드
# reload(kNN)
# kNN.datingClassTest()


#2.5 데이트하기 사이트 예측기 함수
# reload(kNN)
# kNN.classifyPerson()


#필기체 인식 시스템
# reload(kNN)
# testVector = kNN.img2vector('../data/testDigits/0_13.txt')
# print(testVector[0, 0:31])
# print(testVector[0, 32:63])



#2.6 필기체 번호 검사 코드
reload(kNN)
kNN.handwritingClassTest()
