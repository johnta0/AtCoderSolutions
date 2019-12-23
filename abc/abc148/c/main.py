# from fractions import gcd # 3.5 より前
from math import gcd # 3.5 以降

def lcm(x, y):
    return x * y // gcd(x, y)

a, b = map(int, input().split())
print(lcm(a, b))