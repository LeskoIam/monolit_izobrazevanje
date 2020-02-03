# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


# def recursiv():
#     print("noro")
#     recursiv()
#
# recursiv()

def vse_je_objekt():  # Ne uporabljaj!!!!!!!!!!
    print(vse_je_objekt.a)
    print("frei")


vse_je_objekt.a = 3
print(vse_je_objekt.a)
vse_je_objekt()


d = {"f1": vse_je_objekt}

d["f1"]()

