# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class SlovenianLocalizer:
    """A simple localizer"""

    def __init__(self):
        self.translations = {"dog": "pes", "cat": "macka"}

    def localize(self, msg):
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Slovenian": SlovenianLocalizer
    }
    return localizers[language]()  # EnglishLocalizer()


eng, slo = get_localizer("English"), get_localizer("Slovenian")

for word in "dog city cat".split(" "):
    print(eng.localize(word), slo.localize(word))
