#-*- coding:utf-8 -*-

from time import localtime, strftime

logfile = 'test.log'

def writeLog(logfile, log):
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'

    with open(logfile, 'a') as f:
        f.writelines(log)

writeLog(logfile, '첫 번째 로깅 문장입니다.')

