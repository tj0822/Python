# -*- coding:utf-8 -*-
'''
Created on 2015. 10. 7.

@author: TaijinKim
'''

from math import log
from numpy.random.mtrand import operator


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCount = {}
    for featVec in dataSet:
        # print('featVec : ' + str(featVec))
        currentLabel = featVec[-1]
        # print('currentLabel : ' + currentLabel)

        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0
    # print('labelCount : ' + str(labelCount))

    for key in labelCount:
        # print('key : ' + key)
        # print('labelCount[key]) : ' + str(labelCount[key]))
        prob = float(labelCount[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
        # print('prob : ' + str(prob))
        # print(shannonEnt)
    return shannonEnt


def createDataset():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 3.2 주어진 속성으로 데이터 집합 분할하기

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            # print(reducedFeatVec)
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 3.3 데이터 분할 시 가장 좋은 속성 선택하기
def chooseBestFeatureSplit(dataSet):
    # print('dataSet[0] : ' + str(dataSet[0]))
    numFeatures = len(dataSet[0]) - 1
    # print('numFeatures : ' + str(numFeatures))
    baseEntropy = calcShannonEnt(dataSet)
    # print('baseEntropy : ' + str(baseEntropy))
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        # print('featList : ' + str(featList))
        uniqueVals = set(featList)
        # print('uniqueVals : ' + str(uniqueVals))
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    print(bestFeature)
    return bestFeature

# 연구중
def chooseBestFeatureSplit2(dataSet):
    numFeatures = len(dataSet[0]) - 1
    for i in range(numFeatures):
        bestFeature = i
    return bestFeature
# 뭐야


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print("majorityCnt : " + str(sortedClassCount[0][0]))
    return sortedClassCount[0][0]


# 3.4 트리 만들기 코드
def createTree(dataSet, labels):
    # print "dataSet : " + str(dataSet)
    classList = [example[-1] for example in dataSet]
    # print "classList : " + str(classList)
    # print('classList[0] : ' + classList[0])
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureSplit2(dataSet)
    print("bestFeat : " + str(bestFeat))
    bestFeatLabel = labels[bestFeat]
    print('bestFeatLabel : ' + bestFeatLabel)
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


# 3.8 기존의 의사결정 트리를 위한 분류 함수
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


# 3.9 pickle을 가지고 의사결정 트리를 유지시키는 방법
def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
