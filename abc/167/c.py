import numpy as np

n, m, x = map(int, input().split())

C = []
A = [[] for _ in range(n)]
for i in range(n):
    li = list(map(int, input().split()))
    C.append(li[0])
    A[i] = li[1:]

C = np.array(C)
A = np.array(A)

# 全探索

ans = n * 10 ** 5
flag = False
for bit in range(2 ** n):  # bit 1000101010
    money = 0
    levels = np.array([0] * m)
    for j in range(n):  # 0 <= j < n
        if bit >> j & 1:
            money += C[j]
            levels += A[j]
    # すべて x 以上なら
    if np.all(levels >= x):
        flag = True
        ans = min(ans, money)

if flag:
    print(ans)
else:
    print(-1)
