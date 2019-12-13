from concurrent.futures import ThreadPoolExecutor
import time
N = 100
MAX = 10

def work(n):
    sum_ = 0
    for n in range(n):
        sum_ += n**0.3
    return sum_

future = [None]*N

with ThreadPoolExecutor(max_workers=MAX) as executor:
    start = f"started at {time.strftime('%X')}"
    for n in range(N):
        future[n] = executor.submit(work, 10*1000*1000)
    print("this is the main process waiting ...")
    for n in range(N):
        print(future[n].result())
    finish = f"finished at {time.strftime('%X')}"
    print(start)
    print(finish)
