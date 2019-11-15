from functools import reduce


def absValue(x): 
    if x < 0: 
        return -x
    else:
        return x
    
def power(x,p):
    if p == 0: return 1
    if p == 1: return x
    else: return x * power(x,p-1)

def isPrime(x):
    if x == 1 or x == 0: return False
    l = [x % a != 0 for a in range(2,x-1)]
    return reduce(lambda x,y: x and y, l, True)

def slowFib(n):
    if n == 0: return 0
    f = fib2()
    l = [next(f) for _ in range(n+1)]
    return l[-1]

def fib2():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b


