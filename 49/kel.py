#!/usr/bin/env python
def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

if __name__ == '__main__':
    count = counter()
    print count.next()
    print count.next()
    count.send(9)
    print count.next()
    print count.next()
    count.close()

