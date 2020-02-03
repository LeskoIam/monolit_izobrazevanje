# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


def m2f(val):
    return val*3.2808


def f2m(val):
    return val/3.2808


def not_needed(val):
    return val


pretvorbe = {
    "SLO": {"m": not_needed, "ft": f2m},
    "GB": {"m": m2f, "ft": not_needed}
}

# pretvorbe["SLO"]["m"](4)
# {"m": not_needed, "ft": f2m}["m"](4)
# not_needed(4)


class Localize:

    def __init__(self, val, unit):
        self.val = val
        self.unit = unit

    def loc(self, location):
        return pretvorbe[location][self.unit](self.val)
        #                                 f2m()


loc = Localize(2, "m")
print(loc.loc("SLO"))
print(loc.loc("GB"))

loc1 = Localize(6.5, "ft")
print(loc1.loc("SLO"))
print(loc1.loc("GB"))
