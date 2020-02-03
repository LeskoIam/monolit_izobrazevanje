# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


# Same object, shared state

class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Singleton.__instance is None:
            raise Exception("This class is a singleton!")
        return Singleton.__instance

    def __init__(self, path):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

        self.path = path


s = Singleton("c:/test.log")
print(s)

a = Singleton.get_instance()
print(a)

b = Singleton.get_instance()
print(b)

