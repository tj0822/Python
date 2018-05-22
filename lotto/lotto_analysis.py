#-*- coding:utf-8 -*-

from numpy.random import choice
import lotto_stistics as stistics
import lotto_history as history


# 번호 추천
'''
def getLottoNumBySum(lottoDictByNumber, lottoDictBySum):
    # 선택할 sum 숫자수
    pickSumCount = 5
    pSumList = [x / sum(lottoDictBySum.values()) for x in lottoDictBySum.values()]

    # 확률 가중치에 의해 랜덤으로 pickSumCount만큼 추출
    pickSumList = choice(list(lottoDictBySum.keys()), pickSumCount, p=pSumList)

    # 숫자를 합해서 특정 합을 만드는 숫자의 조합 구하기

    # 번호별 분포 확률
    pList = [x / sum(lottoDictByNumber.values()) for x in lottoDictByNumber.values()]

    for n in pickSumList:
        listNumberCombinationBySum = getNumberCombinationListBySum(n)
        s = 0
        for x in listNumberCombinationBySum:
            print(x)
            s += pList[x]
        print(listNumberCombinationBySum, ' :', s)

    # 추천 번호 리스트
    pickNumberList = []

    cnt = 0
    for i in sorted(pickSumList):
        while(cnt < pickSumCount):
            pickNumber = choice(list(lottoDictByNumber.keys()), 6, p=pList)
            if len(set(pickNumber)) == 6:
                if i == sum(pickNumber):
                    print('선택 :', pickNumber)
                    cnt += 1
                    pickNumberList.append(sorted(list(pickNumber)))
                    break
                else:
                    continue

    return pickNumberList
'''

def recommendNumberBySum(lottoDictByNumber, lottoDictBySum):
    # 선택할 sum 숫자수
    pickSumCount = 5

    total = sum(list(lottoDictBySum.values()))
    for key in lottoDictBySum:
        lottoDictBySum[key] = lottoDictBySum[key] / total

    pickSumList = choice(list(lottoDictBySum.keys()), pickSumCount, p=list(lottoDictBySum.values()))

    total = sum(list(lottoDictByNumber.values()))
    for key in lottoDictByNumber:
        lottoDictByNumber[key] = lottoDictByNumber[key] / total

    # 추천 번호 리스트
    pickNumberList = []

    for n in pickSumList:
        # 합이 n인 숫자의 조합과 확률 찾기
        listNumbers = getNumberCombinationListBySum(n)
        pList = []
        for numbers in listNumbers:
            p = 0
            for number in numbers:
                p += lottoDictByNumber[number]

            pList.append(p)

        pList = [x / sum(pList) for x in pList]
        idx = choice(list(range(0, listNumbers.__len__())), 1, p=pList)
        pickNumberList.append(listNumbers[idx[0]])

    return pickNumberList

def getNumberCombinationListBySum(s):
    l = []
    for a in range(1, 46):
        for b in range(a + 1, 46):
            for c in range(b + 1, 46):
                for d in range(c + 1, 46):
                    for e in range(d + 1, 46):
                        for f in range(e + 1, 46):
                            if a + b + c + d + e + f == s:
                                l.append([a, b, c, d, e, f])
    return l

def getLottoNumByNumberCount(lottoDictByNumber):
    # 선택할 sum 숫자수
    pickSumCount = 5

    # 번호별 분포 확률
    pList = [x / sum(lottoDictByNumber.values()) for x in lottoDictByNumber.values()]

    # 추천 번호 리스트
    pickNumberList = []

    cnt = 0
    while (cnt < pickSumCount):
        pickNumber = choice(list(lottoDictByNumber.keys()), 6, p=pList)
        if len(set(pickNumber)) == 6:
            cnt += 1
            pickNumberList.append(sorted(list(pickNumber)))
        else:
            continue


    return pickNumberList

def getRecommendNumbers(lastSeries=None):
    # lotto history 가져오기
    if lastSeries == None:
        lastSeries = history.getLastSeries()
    lottoHistory = stistics.getLottoHistory(lastSeries)

    # 당첨번호 통계 요약정보
    lottoDictByNumber, lottoDictBySum = stistics.getLottoDic(lottoHistory)

    pickNumberList = recommendNumberBySum(lottoDictByNumber, lottoDictBySum)

    return pickNumberList


