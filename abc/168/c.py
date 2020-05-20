import sys
from collections import deque
import bisect
import math
import itertools
from queue import deque
from math import gcd

INF = float('inf')
mod = 10**9+7
eps = 10**-7


def inp(): return int(sys.stdin.readline())


def inp_list(): return list(map(int, sys.stdin.readline().split()))


def lcm(x, y): return (x * y) // gcd(x, y)


A, B, H, M = inp_list()
# H, M = inp_list()

h_ang = (H / 12 + M/ 12 / 60) * 2 * math.pi 
m_ang = M / 60 * 2 * math.pi

ang_diff = abs(h_ang - m_ang)


# print(h_ang)
# print(m_ang)
# print(ang_diff)

ans = math.sqrt(A ** 2 + B ** 2 + 2 * A * B * math.cos(ang_diff))
print(ans)
