import multiprocessing as mp
import os, random, time

# Communication between multiple processes using a queue
# Processes take turns to write to and read from the queue
# Note that it is possible to end up reading your own messages


def randomDelay():
    seed = time.monotonic_ns()
    random.seed(seed)    
    time.sleep(random.random()*5)

# this function is executed in a subprocess
def f(q, name):
    print(f"{name} starting")

    for n in range(10):
        randomDelay();
        # put() on even loops, get() on odd loops
        if n%2 == 0:
            q.put(f"message from {name}")
        else:
            message = q.get()
            lastWordOfMessage = message.split()[2]
            if name == lastWordOfMessage:
                print(f"{name} just read my own message")
            else:
                print(f"{name} just read {message}")

    
def main():
    mp.set_start_method('fork')
    q = mp.Queue()
    N = 10
    children = []
    for n in range(1, N+1):
        child = mp.Process(target=f, args=(q, f"child{n}"))
        children.append(child)
        child.start()
    
    for child in children:
        child.join()
       
main()
