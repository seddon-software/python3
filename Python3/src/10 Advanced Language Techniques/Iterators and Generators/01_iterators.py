############################################################
#
#    iterators
#
############################################################

# iterators must support two methods: __iter__ and __next__

class Fibonacci:
    def __init__(self):
        self.x,self.y = 0,1
        
    def __iter__(self):
        return self  # the object on which to call next() - usually ourself

    def __next__(self):
        if self.x > 100:
            raise StopIteration     # indicate end of iteration
        
        self.x, self.y = self.y, self.x + self.y
        return self.x

# try:
#     iter = Fibonacci()
#      
#     print(iter.__iter__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
#     print(iter.__next__())
# except StopIteration as e:
#     print(e)
    
# create an instance of class and invoke iterator methods
# __iter__(self) will be called once
# __next__(self) will be called until loop terminates


for f in Fibonacci():
    print(f, end=", ")


1







