import time, os
from threading import Thread
from multiprocessing import Process, Pool
import numpy as np
from itertools import chain

def calculate(lo, hi):
    print(f'{os.getpid()}', end=' ')
    sum = 0
    for i in range (lo, hi):
        sum += float(i)**0.3
    return sum   

def jobUsingThreads(threadCount, iterations, count):
    threadList = []
    
    for i in range(1, threadCount+1):
        t = Thread(target = calculate, args = (count//iterations,))
        t.start()
        threadList.append(t)
        
    for t in threadList:
        t.join()

def intervals(duration, parts):
    part_duration = int(duration / parts)
    return [(int(i * part_duration), int((i + 1) * part_duration)) for i in range(parts)]

def jobUsingProcesses(processCount):
    p = Pool(processes=processCount)
    M = 50*1000*1000
    it = intervals(M, processCount)
    result = p.starmap(calculate, it)
    #print(sum(result))


for N in chain(range(1, 9), range(12, 100, 8)):
    start = time.perf_counter()
    jobUsingProcesses(N)
    finish = time.perf_counter()
    print(f"{N}:{finish-start:6.2f}")
