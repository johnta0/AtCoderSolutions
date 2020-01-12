n = int(input())
x = list(map(int, input().split()))

from itertools import permutations

# def factorial(n):
#     ret = 1
#     for i in range(2, n + 1):
#         ret *= i
#     return ret

perm = list(permutations(list(range(1, n)), n - 1))


dp = {}
for tup in perm:
    s = ''.join(list(map(str, tup)))
    for i in range(len(s)):
        try: # dp[s[:i]] が既にある場合
            dummy = dp[s[:i]]
            continue
        except KeyError: # dp[s[:i]] がまだない場合
            dp[s[:i]] = dp[s[:i-1]] + (x[s[i-1]] - x[])
            
        

