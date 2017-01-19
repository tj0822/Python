# -*- coding: utf-8 -*-
'''
Created on 2015. 9. 4.

@author: TaijinKim
'''
from numpy import *
import operator
from os import listdir

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

#2.1 k-최근접 이웃 알고리즘
def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 5
	sortedDistIndicies = distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
		sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	
	return sortedClassCount[0][0]

#2.2 Numpy 구문 분석 코드에 텍스트 기록하기
def file2matrix(filename):
	fr = open(filename)
	numberOfLines = len(fr.readlines())
	returnMat = zeros((numberOfLines, 3))
	classLabelVector = []
	fr = open(filename)
	index = 0
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index, :] = listFromLine[0:3]
		classLabelVector.append(listFromLine[-1])
		index += 1
	return returnMat, classLabelVector

#2.3 데이터 정규화하기 코드 
def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1))
	normDataSet = normDataSet / tile(ranges, (m,1))
	return normDataSet, ranges, minVals


#2.4 데이트하기 사이트를 위한 분류기 검사 코드
def datingClassTest():
	hoRatio = 0.10
	datingDataMat, datingLabels = file2matrix('../data/datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m * hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
		print ("the classifier came back with: %s, the real answer is : %s" % (classifierResult, datingLabels[i]))
		
		if(classifierResult != datingLabels[i]):errorCount += 1.0
		
	print ("the total error rate is :%f" % (errorCount/float(numTestVecs)))
	
	
#2.5 데이트하기 사이트 예측기 함수
def classifyPerson():
	resultList = ['not at all', 'in small doses', 'in large doses']
	percentTats = float(raw_input("percentage of time spent playing video games?"))
	ffMiles = float(raw_input("frequent flier miles earned per year?"))
	iceCream = float(raw_input("liters of ice cream consumed per year?"))
	datingDataMat, datingLabels = file2matrix('../data/datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles, percentTats, iceCream])
	print(inArr)
	classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
	print(classifierResult)
	print ("You will probably like this person : ", resultList[int(classifierResult)-1])
	

# 필기체 인식 시스템
def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0, 32*i+j] = int(lineStr[j])
	return returnVect


#2.6 필기체 번호 검사 코드
def handwritingClassTest():
	hwLabels = []

	trainingFileList = listdir('../data/digits/trainingDigits')
	m = len(trainingFileList)
	trainingMat = zeros((m, 1024))
	
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i, :] = img2vector('../data/digits/trainingDigits/%s' % fileNameStr)
	testFileList = listdir('../data/digits/testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('../data/digits/testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
		print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
		
		if (classifierResult != classNumStr): errorCount += 1.0
	print ("\nthe total number of errors is: %d" % errorCount)
	print ("\nthe total error rate is: %f" % (errorCount/float(mTest)))
	
 