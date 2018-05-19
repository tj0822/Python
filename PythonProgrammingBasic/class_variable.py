#-*- coding:utf-8 -*-

class Circle():
    PI = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    # 원의 면적을 구한다
    def get_area(self):
        area = Circle.PI * (self._radius ** 2)
        return round(area, 2)

    # 원의 둘레를 구한다
    def get_circumference(self):
        circumference = 2 * self.PI * self._radius
        return round(circumference, 2)

if __name__ == '__main__':
    circle1 = Circle(3)
    print('원주율 : ', Circle.PI)
    print('반지름 : ', circle1.radius, '면적 : ', circle1.get_area())
    print('반지름 : ', circle1.radius, '둘레 : ', circle1.get_circumference())

    circle2 = Circle(4)
    print('반지름 : ', circle2.radius, '면적 : ', circle2.get_area())
    print('반지름 : ', circle2.radius, '둘레 : ', circle2.get_circumference())



