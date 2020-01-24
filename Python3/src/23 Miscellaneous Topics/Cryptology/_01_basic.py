# 1. Pick two prime numbers
p = 67
q = 71

# 2. Multiply your primes
n = p * q
print(n)

# 3. Find the least common multiple (lcm) of p-1 and q-1
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
    '''
    The modular multiplicative inverse is an integer ‘x’ such that:
        a * x ≡ 1 (mod m) 
    The value of x should be in {0, 1, 2, … m-1}, 
    i.e., in the range of integer modulo m.
    '''
    t = 0
    new_t = 1
    r = x
    new_r = e
    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
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
