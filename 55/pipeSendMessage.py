#!/usr/bin/env python

from multiprocessing import Pipe,Process

def send(pipe):
    pipe.send('kel')
    pipe.close()

def talk(pipe):
    pipe.send('kel is the best')
    pipe.close()

if __name__ == '__main__':
    conn1,conn2=Pipe()
    sender = Process(target=send,args=(conn1,))
    sender.start()
    print 'recieve :',conn2.recv()
    conn2.close()

    parentEnd,childEnd=Pipe()
    child = Process(target=talk,args=(parentEnd,))
    child.start()
    print 'got',childEnd.recv()
    parentEnd.send([x*2 for x in 'kel'])
    child.join()
    print 'exit'
