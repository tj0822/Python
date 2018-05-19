#-*- coding:utf-8 -*-


class CircleCalculator():
    __PI = 3.14

    # 원의 면적을 구하는 클래스 메서드
    @classmethod
    def calculate_area(cls, radius):
        area = cls.__PI * (radius ** 2)
        return round(area, 2)

    # 원의 둘레를 구하는 클래스 메서드
    @classmethod
    def calculate_circumference(cls, radius):
        circumference = 2 * cls.__PI * radius
        return round(circumference, 2)

if __name__ == '__main__':
    print('반지름 : ', 3, '면적 : ', CircleCalculator.calculate_area(3))
    print('반지름 : ', 3, '둘레 : ', CircleCalculator.calculate_circumference(3))
