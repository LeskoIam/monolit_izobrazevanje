# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class MojPrviClass:

    def __init__(self, a, b):
        self.x = a
        self.test = b
        print("test")
        self.moja_metoda()

    def moja_metoda(self):
        print(self.x)

    def __abs__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        return "izpis"

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


b = MojPrviClass(1, 2)
print(b)
b.moja_metoda()
b.x = 23
print(b.x)
b.jaz = 23
