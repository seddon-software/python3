import copy


x = [[10,11], [20,21], [30,31], [40,41], [50,51]]
y = x[:]        # shallow copy
z = list(x)     # shallow copy
w = copy.copy(x)# shallow copy
v = copy.deepcopy(x)

print(id(x))
print(id(y))
print(id(z))
print(id(w))
print(id(v))

print(id(x[2]))
print(id(y[2]))
print(id(z[2]))
print(id(w[2]))
print(id(v[2]))
