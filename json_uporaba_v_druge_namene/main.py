# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

import configparser
import json
conf_file = r"config.ini"
print(conf_file)

conf = configparser.ConfigParser()
conf.read(conf_file)

d = conf.get("section", "prompts")
print(d, type(d))

d = json.loads(d)

print(d, type(d))
