from collections import  deque
import bisect
import math
import itertools
from queue import deque
from math import gcd

INF = float('inf')
mod = 10**9+7
eps = 10**-7

import sys

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

def lcm(x, y): return (x * y) // gcd(x, y)
