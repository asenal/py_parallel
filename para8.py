import threading

class mythread(threading.Thread):
    def __init__(self,myId,count):
        self.myId = myId
        self.count = count
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            stdoutmutex.acquire()
            print '[%s] -> %s' % (self.myId,i)
            stdoutmutex.release()

stdoutmutex = threading.Lock()
threads = []
for i in range(3):
    thread = mythread(i,3)
    thread.start()
    threads.append(thread)

## - ordered output
#for thread in threads:
#    thread.join()

## - disordered output
map(threading.Thread.join,threads)

print 'Main thread exiting'
