# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Matevz:

    def __init__(self, a: int):
        """Class docstring
        :type a: int

        """
        self.a = a

    def my_func(self, a: str):
        """test function

        :param a: string
        :return: something
        """
        return a*self.a


if __name__ == '__main__':
    m = Matevz(3)
    m.my_func("test")
