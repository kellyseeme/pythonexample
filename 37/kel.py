#!/usr/bin/env poython

import re
p = re.compile("hello")
m = p.match("hello word")

print m.group()
