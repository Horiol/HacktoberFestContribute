#for finding Greatest Common Divisor of two numbers using pyhton
def gcd(a,b):
    return b if a==0 else (b%a, a)
