'''
1. stdout is shared among all threads,the outout of threads is intermixed
'''

import thread,time

def counter(myId, count):
    for i in range(count):
#        time.sleep(1)
        print '[%s]-> %s' % (myId,i)

for i in range(5):
    thread.start_new(counter, (i,3))

time.sleep(2)
print 'main thread exit'
