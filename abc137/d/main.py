n, m = map(int, input().split())

A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
# 今日からM日後まで〜
money = 0
for i in range(m):
    while True:
        mx_delay = max(A)
        idx = A.index(mx_delay)
        if mx_delay < m - i + 1:
            money += B[idx]
            A.pop(idx)
            B.pop(idx)
            break
        if len(A) < 1: break
print(money)
