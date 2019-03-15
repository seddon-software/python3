############################################################
#
#    generators
#
############################################################

# functions that contain yield can produce an iterable
def ids():
    print("ids()")
    for x in [2,3,5,7,11,13,17,19]: 
        yield x
    return

g = ids()
print(g.__next__())
# calling the function produces an iterator
for n in ids():
    print(n)
    
