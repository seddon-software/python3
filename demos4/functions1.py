def square(n):
    # body of the function
    return n**2

def cube(n):
    return n**3

def quad(n):
    return n**4


def power(fn, n):
    return fn(n)


p = 77
print(power(cube           , 7 ))
print(power(quad           , 10))
print(power(lambda n: n**p , 7 ))


