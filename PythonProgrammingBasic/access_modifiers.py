#-*- coding:utf-8 -*-

class Car:
    def __init__(self):
        self.price = 2000
        self._speed = 0
        self.__color = 'red'

if __name__ == '__main__':
    my_car = Car()
    print(my_car.price)
    print(my_car._speed)
    # print(my_car.__color)