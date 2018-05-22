#-*- coding:utf-8 -*-

# 1
# def solution(S):
#     # write your code in Python 3.6
#     n = getNumber(S)
#     cnt = 0
#
#     while(n > 0):
#         cnt += 1
#         if n%2 == 0:
#             n /= 2
#         else:
#             n -= 1
#     return cnt
#
# def getNumber(S):
#     n = 0
#     lenS = S.__len__()
#     for i in range(0, lenS):
#         n += int(S[lenS-i-1]) * (2 ** i)
#     return n
#
# solution('011100')

'''
# 3
def solution(A, B, M, X, Y):
    # write your code in Python 3.6

    stopCnt = 0
    idx = 0
    tempIdx = 0
    personCnt = 0

    while(idx < A.__len__()):
        if personCnt == 0:
            # Ground Floor
            print('G 탑승 : ', [A[idx], B[idx]])
            personCnt += 1
            idx += 1
        elif A[tempIdx:idx].__len__() < X and sum(A[tempIdx:idx]) <= (Y-A[idx]):
            print('탑승 : ', [A[idx], B[idx]])
            personCnt += 1
            idx += 1
        else:
            stopCnt += len(set(B[tempIdx:idx])) + 1
            tempIdx = idx
            personCnt = 0
            print('상승 : ', stopCnt)

    if personCnt > 0:
        print('마지막 탐승자 : ', set(B[tempIdx:idx]))
        stopCnt += len(set(B[tempIdx:idx])) + 1

    return stopCnt



A = [40, 40, 100, 80, 20]
B = [3, 3, 2, 2, 3]
M = 3
X = 5
Y = 200

solution(A, B, M, X, Y)
'''


# 2
def solution(S):
    import pandas as pd

    list = []
    cities = []
    for row in S.split('\n'):
        filename, city, timestamp = row.split(',')
        list.append([city.strip(), filename.split('.')[1], timestamp.strip()])
        cities.append(city.strip())

    cities = set(cities)


    df = pd.DataFrame(list, columns=['city', 'ext', 'timestamp'])
    df['rank'] = df.groupby(['city'])['timestamp'].rank(ascending=True)


    results = ''

    for i in range(0, df.__len__()):
        cnt = int(df[df['city']==city].__len__() / 10) + 1
        result = df['city'][i:i+1] + format(int(df['rank'][i:i+1]), "0" + str(cnt) + "d") + '.' + df['ext'][i:i+1]

        results += result.values[0] + '\n'

        # for row in df[df['city']==city].iterrows():
        #     print(row[1][0] + format(int(row[1][3]), "0"+ str(cnt) + "d") + '.' + row[1][1])
        #     row['result'] = row[1][0] + format(int(row[1][3]), "0"+ str(cnt) + "d") + '.' + row[1][1]

    print(results[:-1])











S = "photo.jpg, Warsaw, 2013-09-05 14:08:15\n" + \
    "ohn.png, London, 2015-06-20 15:13:22\n" + \
    "myFriends.png, Warsaw, 2013-09-05 14:07:13\n" + \
    "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n" + \
    "pisatower.jpg, Paris, 2015-07-22 23:59:59\n" + \
    "BOB.jpg, London, 2015-08-05 00:02:03\n" + \
    "notredame.png, Paris, 2015-09-01 12:00:00\n" + \
    "me.jpg, Warsaw, 2013-09-06 15:40:22\n" + \
    "a.png, Warsaw, 2016-02-13 13:33:50\n" + \
    "b.jpg, Warsaw, 2016-01-02 15:12:22\n" + \
    "c.jpg, Warsaw, 2016-01-02 14:34:30\n" + \
    "d.jpg, Warsaw, 2016-01-02 15:15:01\n" + \
    "e.png, Warsaw, 2016-01-02 09:49:09\n" + \
    "f.png, Warsaw, 2016-01-02 10:55:32\n" + \
    "g.jpg, Warsaw, 2016-02-29 22:13:11"

solution(S)