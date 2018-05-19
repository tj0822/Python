#-*- coding:utf-8 -*-

class Car:
    def __init__(self):
        self._price = 0
        self._speed = 0
        self._color = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

if __name__ == '__main__':
    my_car = Car()

    my_car.price = 2000
    my_car.speed = 20
    my_car.color = 'red'

    print('가격 : ', my_car.price)
    print('속도 : ', my_car.speed)
    print('색상 : ', my_car.color)
