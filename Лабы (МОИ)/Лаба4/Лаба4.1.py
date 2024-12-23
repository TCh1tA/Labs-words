from math import sqrt
import datetime


def root(num):
    try:
        return sqrt(num)
    except(Exception):
        return "Ошибка."


def time():
    return datetime.datetime.now()


print(root(5), time())
# a = datetime.datetime.now()
# for i in range(2, 10000):
#     n = i / i ** 0.5
# b = datetime.datetime.now()
# print(b - a)
