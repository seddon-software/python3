# 1. Pick two prime numbers
p = 67
q = 71

# 2. Multiply your primes
n = p * q
print(n)

# 3. Find the least common multiple (lcm) of p -1 and q -1
import math

def lcm(a, b):
   return a * b // math.gcd(a, b)

x = lcm(p - 1, q - 1)
# x = lcm(67 - 1, 71 - 1)
# x = lcm(66, 70)
# x = 2310
print(x)


# 4. Pick a number less than x that is not a divisor of x:
e = 23

# 5. Compute the modular multiplicative inverse of e:
def inverse_mod(e, x):
   t = 0
   newt = 1
   r = x
   newr = e
   while newr != 0:
       q = r // newr
       t, newt = newt, t - q * newt
       r, newr = newr, r - q * newr
   if r > 1:
       return None
   if t < 0:
       t += x
   return t

d = inverse_mod(e, x)
print(d)

# 6.
public_key = (4757, 23) # (n, e)
private_key = (4757, 1607) # (n, d)

message = 123
encrypted = pow(message, e, n)
decrypted = pow(encrypted, d, n)


print(encrypted)
print(decrypted)
