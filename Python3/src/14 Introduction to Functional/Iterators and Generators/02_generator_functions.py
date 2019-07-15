############################################################
#
#    generators
#
############################################################

# functions that contain yield return an iterator
# by calling said function

def ids():
    x = 1
    while(x < 1000):
        x = x * 2
        yield x
        pass        # just to show execution resumes after the yield
    return

# calling the function produces a genearator (iterator) 
g = ids()

# check that g has both iterator methods
print("Does g have an '__iter__' function:", hasattr(g, "__iter__"))
print("Does g have an '__next__' function:", hasattr(g, "__next__"))

# use g in a loop as an iterator
for n in ids():
    print(n)
    
