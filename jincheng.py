#-*-coding:utf-8-*-
import os
from multiprocessing import Pool
import time,random

def process(name):
    print('now run process %s (%s):' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random())
    end=time.time()
    print('process %s use %s' % (name,(end-start)))



if __name__=='__main__':
    print('now is process %s' % os.getpid() )
    p=Pool(6)
    for i in range(8):
        p.apply_async(process,args=(i,))
    p.close()
    p.join()
    print("end")