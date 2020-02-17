# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
from dataclasses import dataclass
from typing import Union, Optional


@dataclass
class Oseba:
    ime: str
    priimek: str
    visina: Union[int, float]


oseba = Oseba(ime="Matevž", priimek="Test", visina=12)
print(oseba)

exit()

print(type(oseba.visina))


def oegf(ime: str, priimek: Optional[str] = None) -> Union[int, str]:
    if priimek is not None:
        print(priimek)
        return 1
    print(ime)
    return "test"


if __name__ == '__main__':
    os2 = Oseba(oegf("Matevz", "gdfgdf"), "fref", 12)
