#!/bin/bash

# This is a command to generate directory for AtCoder Beginner Contest
if [ $# -ne 1 ]; then
    echo "The number of arguments should be 1."
    exit 1
fi

mkdir abc/$1/

arr=('a' 'b' 'c' 'd' 'e' 'f')
for alph in ${arr[@]}; do
    echo "from collections import  deque
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
    " > abc/$1/$alph.py
    touch abc/$1/$alph.cc
done
