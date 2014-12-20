'''
waiting for spawned thread exits
'''

import thread,time
def counter(myId,count):
    for i in range(count):
        stdoutmutex.acquire()
        print '[%s]-> %s' % (myId,i)
        stdoutmutex.release()
    exitmutexes[myId].acquire()

stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock()] * 5
for i in range(5):
    thread.start_new(counter, (i,5))

for mutex in exitmutexes:
    while not mutex.locked():pass

time.sleep(2)
print 'main thread exiting'
