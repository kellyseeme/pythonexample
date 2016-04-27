#!/usr/bin/env python
import sys,urllib,urllib2,json
import requests

url = 'http://www.tngou.net/tnfs/api/list'
src_header = 'http://tnfs.tngou.net/image'
params_1 = dict(page=3,rows=10,id=6)

r = requests.get(url)

r = r.json()
def saveImage(imgUrl,imgName='default.jpg'):
    reponse = requests.get(imgUrl)
    image = reponse.content
    dst = "g:\\baidu_img\\"
    path = dst+imgName
    print 'save the file :'+path+'\n'
    with open(path,'wb') as img:
        img.write(image)

def run():
    for line in r['tngou']:
        title = line['title']
        print title
        img = line['img']
        src_path = src_header+img
        name = title + '.jpg'
        saveImage(src_path,name)

run()
