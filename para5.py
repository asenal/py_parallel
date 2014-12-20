'''
synchronizing access to global objects

1. theads come with a cross-task communications mechanism called: shared global memory.
2. thread.allocate_lock creates a lock object that is acquired and released by each thread
3. use allocate_lock to get a synchronized stdout among threads
4. do work that doesn't depend on global shared resource first, they will run in parallel,
then work depend on GSR, will be synchronized by lock, successively.
'''

import thread, time

def counter(myId,count):
    for i in range(count):
        #  work you want all threads do  parallelly
        time.sleep(1)

        # work depend on global shared resource will be synchronized by lock, successively
        mutex.acquire()
        print '[%s]-> %s' % (myId,i)
        mutex.release()


mutex = thread.allocate_lock()

for i in range(5):
    thread.start_new(counter, (i,3))

time.sleep(6)
print 'main thread exit'
