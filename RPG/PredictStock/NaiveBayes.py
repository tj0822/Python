#-*- coding:utf-8 -*-

from numpy import *

# 모듬 문서에 있는 모든 유일한 단어 목록을 생성(set)
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        # print('document : ', document)
        # print(document['wordList'])
        vocabSet = vocabSet | set(document['wordList'])  # | : 집합 유형 변수 합치기
    return list(vocabSet)

# 주어진 문서 내에 어휘 목록에 있는 단어가 존재하는지 아닌지를 표현하기 위해 어휘 목록, 문서 1과 0의 출력벡터 사용
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            # print("word : ", word)
            returnVec[vocabList.index(word)] = 1
        else:
            pass
            # print("the word: %s is not in my Vocabulary!" % word)
    # print("returnVec : " + str(returnVec))
    return returnVec

#4.2 나이브 베이스 분류기 훈련 함수
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    # print("numTrainDocs : " + str(numTrainDocs))
    numWords = len(trainMatrix[0])
    # print("numWords : " + str(numWords))
    # print("trainCategory : " + str(trainCategory))
    # print("sum(trainCategory) : " + str(sum(trainCategory)))
    # print("float(numTrainDocs) : " + str(float(numTrainDocs)))
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # print("pAbusive : " + str(pAbusive))
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    # print("range(numTrainDocs) : " + str(range(numTrainDocs)))
    for i in range(numTrainDocs):
        # print("trainCategory[" + str(i) + "] : " + str(trainCategory[i]))
        if trainCategory[i] == 1:
            # print("trainMatrix[" + str(i) + "] : " + str(trainMatrix[i]))
            p1Num += trainMatrix[i]
            # print("p1Num : " + str(p1Num))
            p1Denom += sum(trainMatrix[i])
            # print("p1Denom : " + str(p1Denom))
        else:
            # print("trainMatrix[" + str(i) + "] : " + str(trainMatrix[i]))
            p0Num += trainMatrix[i]
            # print("p0Num : " + str(p0Num))
            p0Denom += sum(trainMatrix[i])
            # print("p0Denom : " + str(p0Denom))
    # print("p1Num / p1Denom = " + str(p1Num) + "/" + str(p1Denom))
    # print("p0Num / p0Denom = " + str(p0Num) + "/" + str(p0Denom))
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    # print("p1Vect : " + str(p1Vect))
    # print("p0Vect : " + str(p0Vect))
    return p0Vect, p1Vect, pAbusive


#4.3 나이브 베이스 분류 함수
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    # print("vec2Classify * p1Vec : " + str(vec2Classify * p1Vec))
    # print("vec2Classify * p0Vec : " + str(vec2Classify * p0Vec))
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    # print("p1 : ", p1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    # print("p0 : ", p0)
    if p1 > p0:
        return 1
    else:
        return 0