from multiprocessing import Pool
import os

    
# this function is excecuted in parallel by a pool of processes
def f(x):
    return x**2

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, range(20)))
        
