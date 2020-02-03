# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Zgradba:

    def __init__(self, st_vrat, st_oken):
        self.st_vrat = st_vrat
        self.st_oken = st_oken

    def __str__(self):
        return f"St. vrat: {self.st_vrat}\nSt. oken: {self.st_oken}"

    def dodaj_vrata(self, n=1):
        self.st_vrat += n  # self.st_vrat = self.st_vrat + n


class Hisa(Zgradba):

    def __init__(self, st_vrat, st_oken, vrt):
        self.vrt = vrt
        # Zgradba.__init__(self, st_vrat, st_oken)
        super(Hisa, self).__init__(st_vrat, st_oken)

    def __str__(self):
        return f"{super(Hisa, self).__str__()}\nVrt: {self.vrt}"




zg = Zgradba(1, 3)
print(zg)
zg.dodaj_vrata()
print(zg)
zg.dodaj_vrata(10)
print(zg)

hisa = Hisa(5, 16, True)
print(hisa)
