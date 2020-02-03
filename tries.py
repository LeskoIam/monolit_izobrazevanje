# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

a = 1
b = 2

print(a)

print(a + b)
c = a + b
print(a * b)

print(1/2)  # deljenje
print(1//2)  # celostevilsko deljenje

print(a**2)

a = 1.2
b = 2.3
c = 1.

print(10./3.)

a = "moje ime"

print(a.capitalize())
print(a.index("j"))
print(len(a))
print(a[3])
print(a[-1])
print(a[1:])
print(a[:-2])
print(a[1:-2])
print(a[1:-2:2])

print(5 % 2)


ime = "Matevz"
starost = 12

output = f"Jaz sem {ime}, star sem {starost}"
print(output)

True
False


a = []
a = [1, 2, 3, 4]
print(a)
a.append(5)
print(a)
a.insert(2, "test")
print(a)
len(a)

b = a.pop(0)
print(a)
print(b)

a.append([5, 6, 7, 8])
print(a)
print(a[-1][-2])
a.remove("test")
print(a)

a = (1, 2, 3)  # tuplpe

f = [1, 2, 3, 3, 4, 4, 5, 5]
g = list(set(f))
print(g)

a = {1, 2, 3, 4}  # set

d = {"kljuc": "vrednost",
     "vrednos2": 2,
     2: {"fjire": [2, 3, 4]}}

print(d)

print(d["kljuc"])
print(d[2]["fjire"][1])

d["nov kljuc"] = 22

print(d)

print("kljuc" in d)


print(d.get("greta", "ni grete"))
a = d.fromkeys([1, 2, 3], 2)

print(a)

print(str(22))
print(int("22"))
print(float("1"))

list()
tuple()
set()
int()
float()
str()
dict()

print(type("fdged"))

print(isinstance("fjdiu", str))

a = ["ofiodf", "fnijdn", "fgker"]

a = "test me now".split(" ")
a = list(map(int, "1 2 3 4 4 5".split(" ")))
print(a)

