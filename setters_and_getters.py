# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import random


class A:

    def __init__(self):
        self.__a = 0



    @property
    def a(self):
        if self.__a < 100:
            return self.__a + 5
        return self.__a

    @a.setter
    def a(self, t):
        self.__a = t*10


if __name__ == '__main__':
    obj = A()
    print(obj)

    obj.a = 100
    print(obj.a)
