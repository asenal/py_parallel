'''
1. start 5 copies of this program
2. child process have a copy of the programme and variables, but won't run from start to end. it runs from os.fork() to os._exit().
'''
import os,time
from random import random
def counter(count):
    for i in range(count):
        time.sleep(random())
        print '[%s] => %s' % (os.getpid(),i)

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print 'Process %d spawned' % pid
    else:
        counter(3)
        print "child process exit"
        os._exit(0)

print "main process exit first"
