import numpy as np

"""
    H: モンスター体力, N = 魔法の種類
    A: i番目の魔法の攻撃力, B: i番目の魔法の消耗
"""
H, N = map(int, input().split())
A, B = [0] * N, [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

A = np.array(A)
B = np.array(B)

cost = B / A
cost_order = np.argsort(cost)

A_srtd = A[cost_order]
B_srtd = B[cost_order]

ans = 0
for i in range(N):
    a = A_srtd[i]
    b = B_srtd[i]
    div_cnt = H // a
    H -= div_cnt * a
    
    ans += b * div_cnt
    if H < 1: break

    if i != N - 1 and A_srtd[i + 1] >= H and B[i + 1] < B[i]:
        continue
    else:
        ans += b
    
    if H < 1: break

print(ans)