#!/usr/bin/env python

from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42,None,'kel'])
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()
    print parent_conn.recv()
    p.join()
