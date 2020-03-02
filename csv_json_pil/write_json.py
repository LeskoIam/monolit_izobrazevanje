# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import json

data = {"telephone": [{"operator": "mobitel",
                       "number": "070123456"}],
        "address": "soncna ulica 1"}

print(json.dumps(data, indent=4))

with open("test.json", "w") as f:
    json.dump(data, f)
