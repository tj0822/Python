#-*- coding:utf-8 -*-

class Car(object):
    def __init__(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    def start(self):
        self._speed = 20

    def accelerate(self):
        self._speed += 30

    def stop(self):
        self._speed = 0

class SportCar(Car):
    def __init__(self):
        self._color = 'red'

    def accelerate(self):
        self._speed += 40

    def turbocharge(self):
        self._speed += 70

    @property
    def color(self):
        return self._color

if __name__ == '__main__':
    my_sportcar = SportCar()
    print('색상 : ', my_sportcar.color)
    my_sportcar.start()
    print('속도 : ', my_sportcar.speed)
    my_sportcar.accelerate()
    print('속도 : ', my_sportcar.speed)
    my_sportcar.turbocharge()
    print('속도 : ', my_sportcar.speed)
    my_sportcar.stop()
    print('속도 : ', my_sportcar.speed)
