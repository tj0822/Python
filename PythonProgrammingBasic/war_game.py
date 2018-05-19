#-*- coding:utf-8 -*-

from PythonProgrammingBasic.fighter import Fighter
from PythonProgrammingBasic.bomber import Bomber

def war_game(airforce):
    airforce.take_off();
    airforce.fly()
    airforce.attack()
    airforce.land()

if __name__ == '__main__':
    f15 = Fighter(3)
    war_game(f15)
    print()

    b29 = Bomber(3)
    war_game(b29)



