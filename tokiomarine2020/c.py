import numpy as np

n, k = map(int, input().split())
A = np.array(list(map(int, input().split())))

plus = np.zeros(n, dtype=int)

for _ in range(k):
    for i in range(n):
        a = A[i]
        print(a)
        left = max(0, i - a)
        right = min(n - 1, i + a)
        plus[left:right + 1] += 1
        print(plus)
A += plus
print(*A)
