K = int(input())

from collections import deque
q = deque(range(1, 10))
for _ in range(K - 1):
    d = q.popleft()
    if d % 10 > 0:
        q.append(d * 10 + d % 10 - 1)
    q.append(d * 10 + d % 10)
    if d % 10 < 9:
        q.append(d * 10 + d % 10 + 1)
print(q.popleft())
