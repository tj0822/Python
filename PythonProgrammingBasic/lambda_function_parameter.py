#-*- coding:utf-8 -*-

def circle_area(radius, function_param):
    area = 3.14 * (radius ** 2)
    function_param(area)

if __name__ == '__main__':
    circle_area(3, lambda x: print('결과값', round(x, 1)))
    circle_area(3, lambda x: print('결과값', round(x, 2)))
