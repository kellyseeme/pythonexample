#!/usr/bin/env python

import multiprocessing

def func(conn):
    #conn.send('kel')
    conn.close()

def f(q,l):
    q.put('kel')
    l.append('kel')

if __name__ == '__main__':
    l = []
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=f,args=(q,l))
    p.start()
    print q.get()
    print l
    p.join()

    parent_conn,child_conn = multiprocessing.Pipe()
    kel = multiprocessing.Process(target=func, args=(child_conn,))
    kel.start()
    print parent_conn.recv()
    kel.join()
