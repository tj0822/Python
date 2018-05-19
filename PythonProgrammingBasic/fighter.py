#-*- coding:utf-8 -*-

from PythonProgrammingBasic.airforce import AirForce

class Fighter(AirForce):
    def __init__(self, weapon_num):
        self._missile_num = weapon_num

    def take_off(self):
        print('전투기 발진')

    def fly(self):
        print('전투기가 목표지로 출격')

    def attack(self):
        for i in range(self._missile_num):
            print('미사일 발사')
            self._missile_num -= 1

    def land(self):
        print('전투기 착륙')





