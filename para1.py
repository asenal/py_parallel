'''
1. os.fork() will start a child process  running the same code copy as its parent process
2. os.fork() will child process a pid, but child process doesn't know it. it's zero in child process.'
3. parent process(the caller of os.fork) knows the pid of the process
4. the parent process live untill a input 'q', the child process is killed by os._exit(0). otherwise it's gonna make a huge tree and run out system resources
'''
import os
from random import random
def child():
    print "hello from child", os.getpid()
    os._exit(0)

def parent():
    while 1:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print "hello from parent", os.getpid(),newpid

        if raw_input() == 'q':break

if __name__ == '__main__':
    parent()
