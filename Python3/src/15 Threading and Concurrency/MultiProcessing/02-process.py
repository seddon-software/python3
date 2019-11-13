from multiprocessing import Process
import os, random, time


# Here we execute a function in separate processes


def randomDelay():
    seed = time.monotonic_ns()
    random.seed(seed)    
    time.sleep(random.random()*5)
    
# this function is excecuted in parallel by eachprocesses
def f(x):
    randomDelay()
    print(f"{os.getppid()} --> {os.getpid()} : {x**2}")

def main():
    print(f" ppid --> pid   : x**2")
    processes = []
    for n in range(10):
        p = Process(target=f, args=(n,))
        p.start()
        processes.append(p)

    for n in range(10):
        p.join()
        
main()

