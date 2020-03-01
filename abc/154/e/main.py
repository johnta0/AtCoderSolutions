N = int(input())
K = int(input())
L = len(str(N))

from math import factorial
def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))

ans = 0
for l in range(1, L + 1):
    if l < K:
        continue
    if l == 1 and N > 9:
        ans += 9
    elif L == l:
        ans += 
    else:
        ans += (combinations_count(l - 1, K  - 1)) * 9 ** K

print(ans)