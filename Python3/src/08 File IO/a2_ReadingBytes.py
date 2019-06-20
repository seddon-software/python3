fileName = "data/myfile-1.bin"
f = open(fileName, "rb")
x = f.read()
print(type(x), x) 
print(list(x))
