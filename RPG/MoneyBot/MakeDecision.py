#-*- coding:utf-8 -*-
import RPG.MoneyBot.AibrilNLU as alu

# -1: sell 0:stay 1:buy
def GetAbrilALUscore(stock, stockName, date):
    return alu.getScore(stock, stockName, date)