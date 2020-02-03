# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


# Different object, shared state

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):

    def __init__(self):
        super(YourBorg, self).__init__()


borg1 = Borg()
borg2 = Borg()

borg1.state = "Idle"
borg2.state = "Running"

print(borg1)
print(borg2)

borg3 = YourBorg()
borg3.state = "Picard"

print(borg1)
print(borg2)
print(borg3)

print(repr(borg1))
print(repr(borg2))
print(repr(borg3))
