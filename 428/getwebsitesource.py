#!/usr/bin/env python

import urllib
import urllib2

url= 'https://github.com/ansible/ansible/commit/f31421576b00f0b167cdbe61217c31c21a41ac02'
url = 'https://mp.weixin.qq.com/'
value = {'account':'402111939@qq.com','password':'1qaz@WSX'}
data = urllib.urlencode(value)
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
f = open('kel.txt','w')
for i in response:
    f.write(i)
f.close()
print response.read()

