def inc(a):
    a = a + 1
    return a
        
x = 100
x = inc(x)
print(x)


def addToEnd(l):
    l.append(99)
    
mylist = [10, 11, 12, 13]
print(id(mylist))
addToEnd(mylist)
print(mylist)
