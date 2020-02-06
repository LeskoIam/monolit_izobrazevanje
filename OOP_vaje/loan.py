from typing import Optional, Union

# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Loan:

    def __init__(self, amount: Union[int, float], months: int):
        """Based on loan amount and months to pay off
           calculate amount left

        :param amount: loan amount
        :param months: alimony months
        """
        self.amount = amount
        self.months = months

    def owed_amount(self, months: Optional[int] = None) -> Union[float, int]:
        """Calculate amount owned.

        :param months: how many months we already payed off
        :return: jhfsdkhig
        """
        if months is None:
            return self.amount
        return self.amount - (months*(self.amount/self.months))


if __name__ == '__main__':
    l = Loan(100000, 120)
    print(l.owed_amount())
    print(l.owed_amount(90))
