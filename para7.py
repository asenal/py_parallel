import thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [0] * 3

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print '[%s] -> %s' % (myId,i)
        stdoutmutex.release()
    exitmutexes[myId] = 1 # signal main thread

for i in range(3):
    thread.start_new(counter, (i,3))

while 0 in exitmutexes: pass  # repeat while-loop till no 0 in exitmutexes
print 'main thread exiting'
