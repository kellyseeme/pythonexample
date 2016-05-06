#!/usr/bin/env python

from multiprocessing import Process,Pipe

def fun(pipe,x):
    pipe.send('hello,'+x)

reciver,sender = Pipe()
proc = Process(target=fun,args=(sender,'kel',))
proc.start()
print reciver.recv()
proc.join()
print reciver.recv()
