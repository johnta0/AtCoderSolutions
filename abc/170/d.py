N = int(input())
A = list(map(int, input().split()))
A.sort()

import math

def is_prime(n): # O(sqrt(N))
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def count_num(n, l):
    cnt = 1
    for i in range(1, len(l)):
        if l[i] != n:
            return cnt
        cnt += 1
    return cnt

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

ans = 0
i = 0
while i < N:
    cnt_n = count_num(A[i], A[i:])
    if cnt_n != 1:
        i += cnt_n
        continue
    if A[i] == 1 or is_prime(A[i]):
        ans += 1
        # print('+1:', A[i])
        i += 1
        continue
    
    # not prime
    # flag = True
    # for num in A[:i]:
    #     if math.gcd(num, A[i]) != 1:
    #         i += 1
    #         flag = False
    #         break
    # judge
    flag = True
    for num in A[:i]:
        if A[i] % num == 0:
            flag = False

    if flag:
        # print("+1. x:", A[i])
        ans += 1
    i += 1

print(ans)
