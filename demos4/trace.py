# decorator
def trace(fn):
    def newFn(n):
        print(f"calling {fn.__name__} with {n}")
        return fn(n)
    return newFn

@trace
def square(n):
    return n**2

@trace
def cube(n):
    return n**3

@trace
def quad(n):
    return n**4

# print( trace(square)(3) )
print(  square(3)  )

