#-*- coding:utf-8 -*-

from PythonProgrammingBasic.airforce import AirForce

class Bomber(AirForce):
    def __init__(self, bomb_num):
        self._bomb_num = bomb_num

    def take_off(self):
        print('폭격기 발진')

    def fly(self):
        print('폭격기 목적지로 출격')

    def attack(self):
        for i in range(self._bomb_num):
            print('폭탄 투하')
            self._bomb_num -= 1

    def land(self):
        print('폭격기 착률')