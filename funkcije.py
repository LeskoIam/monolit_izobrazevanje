# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
a = 1


def ime_funkcije():
    print("hello world")


def f_z_argumentom(a, b):
    return a*b


print(f_z_argumentom(1, 2))
print(f_z_argumentom(b=2, a=1))


def f_privzeto(a, b=4):
    return a+b


print(f_privzeto(5))
print(f_privzeto(5, 10))
print(f_privzeto(b=3, a=10))


def vse(a, b=2, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


vse(1, 2, 3, 4, 5, c=10, d=11)


def join(*args):
    return " ".join(args)


a = join("test", "34", "lesko", "zoutube")
print(repr(a))

b = ["test", "34", "lesko", "zoutube"]

print(join(*b))


def poizkusime(**kwargs):
    print(kwargs)


d = {"a": 4, "b": 5}
poizkusime(**d)


def alives(a, s=[]):
    s.append(a)
    return s


print(alives(1))
print(alives(22))
print(alives(666))


