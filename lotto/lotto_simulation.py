#-*- coding:utf-8 -*-

import lotto_analysis as analysis
import lotto_stistics as stistics
import lotto_history as history

def simulation(lastSeries=None):
    if lastSeries == None:
        lastSeries = history.getLastSeries()

    for i in range(700, lastSeries+1):
        recommendNumbers = analysis.getRecommendNumbers(lastSeries)

        print(str(i), '회 추천 :', recommendNumbers)
        result = stistics.getLottoResult(i)[0]
        print(result[1:7], result[7:8])
        for number in recommendNumbers:
            matchCnt = set(number).intersection(set(result[1:7])).__len__()
            if matchCnt < 3:
                print('꽝 :', number)
            elif matchCnt == 3:
                print('5등 :', number)
            elif matchCnt == 4:
                print('4등 :', number)
            elif matchCnt == 5:
                if set(number).difference(result[2:8]) ==  set(result[7:8]):
                    print('2등 :', number)
                else:
                    print('3등 :', number)
            elif matchCnt == 6:
                print('*********1등********* :', number)


simulation()