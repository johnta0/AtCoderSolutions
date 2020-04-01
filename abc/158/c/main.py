from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import copy
import time
import numpy as np
from fractions import gcd

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

def lcm(x, y): return (x * y) // gcd(x, y)


a, b = inp_list()
for n in range(1251):
    wo_tax_a = int(n * 0.08)
    wo_tax_b = int(n * 0.10)
    if wo_tax_a == a and wo_tax_b == b:
        print(n)
        exit()
print(-1)
