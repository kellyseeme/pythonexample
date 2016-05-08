#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json

j = json.loads(open('kel.txt').read())
print type(j),j
