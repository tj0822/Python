#-*- coding:utf-8 -*-

import lotto_statistics as statistics
import random
import lotto_generator as gen

# 로또 당첨번호 이력 가져오기
lotto_history = statistics.getLottoAllResult()

# 번호 dictionary만들기
'''
lottoDictByNumber = {}
for i in range(46):
    lottoDictByNumber[i] = 0
'''

# 시뮬레이션(2~n차)
# print(lotto_history['series'].max())


simCnt = 0
# for i in range(2, lotto_history['series'].max()+1):



def Simulate(func=None):
    flag = True
    simCnt = 0
    resultFileName = 'result_by_' + func.__name__ + '.csv'
    fp = open(resultFileName, 'w', encoding='utf-8')
    fp.write('simCnt,0,1,2,3,4,5_0,5_1,6\r\n')
    while (flag):
        simCnt += 1
        hitCntDic = {0: 0, 1: 0, 2: 0, '5등': 0, '4등': 0, '3등': 0, '2등': 0, '1등': 0}
        for row in lotto_history.iterrows():
            # 추천 번호 생성
            # set(recommendedNumbers).intersection(set())
            recommendedNumberList = func(cnt=10, lottoHistory=lotto_history, series=row[1][0])
            # print(recommendedNumberList)

            for number in recommendedNumberList:
                hitCnt = set(list(row[1][1:7])).intersection(number).__len__()

                if hitCnt == 6:
                    print('********************* 1등 *********************')
                    print(row[1][0], '회 당첨번호 :', list(row[1][1:8]), '당첨금 :', row[1][9])
                    print(number)
                    hitCntDic['1등'] += 1
                elif hitCnt == 5:
                    if set(list(row[1][1:8])).intersection(number).__len__() == 6:
                        # print('*********** 2등 ***********')
                        # print(row[1][0], '회 당첨번호 :', list(row[1][1:8]))
                        # print(number)
                        hitCntDic['2등'] += 1
                        # flag = False
                        # break
                    else:
                        # print('****** 3등 ******')
                        hitCntDic['3등'] += 1
                elif hitCnt == 4:
                    # print('4등')
                    hitCntDic['4등'] += 1
                elif hitCnt == 3:
                    # print('5등')
                    hitCntDic['5등'] += 1
                else:
                    # print('꽝')
                    hitCntDic[hitCnt] += 1

        result = list()
        result.append(simCnt)
        result.extend(list(hitCntDic.values()))
        print(result)
        fp.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\r\n'.format(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8]))
    fp.close()

# Simulate(gen.GenByRandom)
Simulate(gen.GenByNumCnt)