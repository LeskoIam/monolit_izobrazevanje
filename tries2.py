# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

a = 2
if 1 == a:  # if True:
    print("resnicno")
elif 2 == a:
    print("resnicno 2")
elif 3 == a:
    print("resnicno 3")
else:
    print("ni resnicno")

if True:
    print("fkieo")
if 1 == 1:
    print("jfioejo")
else:
    print("fioe")

a = 4
b = 8
if (a % 2 == 0) and (b % 2 == 0):
    print("obe deljivi z 2")

while True:
    print("kldfgjdf")
    break

n = 1
while n < 10:
    print(n)
    if n == 5:
        break
    n += 1  # n = n + 1


print("\n")
n = 10
while n != 0:
    n -= 1
    if n < 5:
        continue
    print(n)


for n, janez_kranjski in enumerate(range(10, 20), 1):
    print(f"{n} - {janez_kranjski}")

for c in "kfjgjdfgldfgldf":
    print(c)

d = {1: "t", 2: "r"}
for key, value in d.items():
    print(f"{key}, {value}")
else:
    print("test")

with open("ime.txt", "w") as text_file:
    text_file.write("test")
    text_file.write("test\n")

text_file = open("ime.txt", "r")
print(text_file.read())
text_file.close()

