#-*- coding:utf-8 -*-

import lotto_analysis as analysis
import lotto_statistics as statistics


hitCnt = {0: 0, 1: 0, 2: 0, '5등': 0, '4등': 0, '3등': 0, '2등': 0, '1등': 0}

# lotto history 가져오기
lottoHistory = statistics.getLottoAllResult()
lastSeries = lottoHistory.tail(1)['series'].values[0]



def simulation():

    for i in range(2, lastSeries+1):
        # 당첨번호 통계 요약정보
        lottoDictByNumber, lottoDictBySum = statistics.getLottoDic(lottoHistory[lottoHistory['series'] < i])
        recommendNumbers = analysis.getRecommendNumbers(lottoDictByNumber, lottoDictBySum)

        # print(str(i), '회 추천 :', recommendNumbers)
        result = statistics.getLottoAllResult()
        # print(result[1:7], result[7:8])
        for number in recommendNumbers:
            matchCnt = set(number).intersection(set(result[1:7])).__len__()
            if matchCnt < 3:
                # print('꽝(', matchCnt, '개 일치', ')', ' :', number)
                hitCnt[matchCnt] += 1
            elif matchCnt == 3:
                # print('5등 :', number)
                hitCnt['5등'] += 1
            elif matchCnt == 4:
                # print('4등 :', number)
                hitCnt['4등'] += 1
            elif matchCnt == 5:
                if set(number).difference(result[2:8]) ==  set(result[7:8]):
                    # print('2등 :', number)
                    hitCnt['2등'] += 1
                else:
                    # print('3등 :', number)
                    hitCnt['3등'] += 1
            elif matchCnt == 6:
                print(str(i), '회 추천 :', recommendNumbers)
                print('*********1등********* :', number)
                hitCnt['1등'] += 1
        # print(hitCnt)

i = 0
while(hitCnt['1등'] == 0):
    i += 1
    print('loop 횟수 : ', str(i))
    simulation()
    print(hitCnt)
    hitCnt = {0: 0, 1: 0, 2: 0, '5등': 0, '4등': 0, '3등': 0, '2등': 0, '1등': 0}




