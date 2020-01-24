def f1():
    print("lib f1")

def f2():
    print("lib f2")

def f3():
    print("lib f3")

def f4():
    print("lib f4")

# tests
print(f"library module name = {__name__}")
if __name__ == "__main__":
    f1()
    f2()
    f3()
    f4()
