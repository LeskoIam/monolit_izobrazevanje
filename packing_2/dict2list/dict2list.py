# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
from typing import List, Tuple, Optional, Callable


def dict2list(input_dict: Optional[dict] = None) -> List[Tuple]:
    """Transform dictionary to list of tuples.

    :param input_dict: dictionary to transform
    :return: list of tuples
    """
    temp_list = []
    for el in input_dict.items():
        temp_list.append(el)
    return temp_list


if __name__ == '__main__':
    d = {"a": 1, "b": 2, "c": 3}

    print(dict2list(d))  # -> [(key, value), (key, value),....]

    print("-".join(["fd", "fd"]))
