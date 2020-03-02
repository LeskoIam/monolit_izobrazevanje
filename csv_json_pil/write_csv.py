# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import csv

with open("test01.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["ena", "dva"])
    for x in range(10):
        w.writerow([1, x, 3, 4])


with open("test02.csv", "w", newline="") as f:
    w = csv.DictWriter(f, ["test", "ime"], delimiter=";")
    w.writeheader()
    for x in range(10):
        w.writerow({"test": x, "ime": "lesko", "test1": "podatek"})
