from multiprocessing import Process, Pipe
import os, random, time

# Communication between parent and child using pipes


# According to the docs, the child should close the pipe and the parent should check:
#     child_connection.closed
# However these operations don't seem to do anything.  
# The pipe is closed automatically when the child exits 

def child(connection):
    message = connection.recv()
    print(message)
    
    for n in range(10):
        connection.send(n**2)
    connection.send("end")

def main():
    parent_connection, child_connection = Pipe()
    p = Process(target=child, args=(child_connection,))
    p.start()
    
    # wait for 5 secs and then tell the child to start
    message = None
    time.sleep(5)
    parent_connection.send("start")
    while message != "end":
        message = parent_connection.recv()
        print(message)
    
    p.join()
        
main()
