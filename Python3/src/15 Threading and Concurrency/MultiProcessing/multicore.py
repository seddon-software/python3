from multiprocessing import Pool, cpu_count

def random_calculation(x):
    while True:
        x * x

#p = Pool(processes=cpu_count())
p = Pool(processes=40)
p.map(random_calculation, range(cpu_count()))


'''
multiprocessing is a package that supports spawning processes using an API similar to the threading module. 
The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global 
Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows 
the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.

CPython implementation detail: In CPython, due to the Global Interpreter Lock, only one thread can execute Python 
code at once (even though certain performance-oriented libraries might overcome this limitation). If you want your 
application to make better use of the computational resources of multi-core machines, you are advised to use 
multiprocessing. However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.

asyncio is a library to write concurrent code using the async/await syntax.  asyncio is used as a foundation for 
multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection 
libraries, distributed task queues, etc.  asyncio is often a perfect fit for IO-bound and high-level structured network code.
'''