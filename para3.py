'''
1. thread share not copy
2. parent process doesn't quit until all threads quit'
'''

import thread

def child(tid):
    print 'hello  from thread', tid

def parent():
    i = 0
    while 1:
        i = i+1
        thread.start_new(child,(i,))
        if raw_input() == 'q':
            print "main process exit"
            break

parent()
