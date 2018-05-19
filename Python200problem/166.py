#-*- coding:utf-8 -*-

def getTextFreq(filename):
    with open(filename, 'r') as f:
        text = f.read()
        fa = {}
        for c in text:
            if c in fa:
                fa[c] += 1
            else:
                fa[c] = 1

    return fa

ret = getTextFreq('5674-734/mydata.txt')
ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)
for c, freq in ret:
    if c == '\n':
        continue
    print('[%c] -> [%d]회 나타남' %(c, freq))