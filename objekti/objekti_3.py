from math import pi

# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Krog:

    def __init__(self, r):
        self.r = r

    def area(self):
        return pi*(self.r**2)

    def circumference(self):
        return 2*pi*self.r


krog = Krog(3)
print(krog.area())
print(krog.circumference())
