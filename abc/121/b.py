import numpy as np

n, m, c = map(int, input().split())
B = np.array(list(map(int, input().split())))

ans = 0
for i in range(n):
    sum = 0
    A = np.array(list(map(int, input().split())))
    sum += np.dot(A, B)
    if sum > -c: ans += 1
print(ans)
