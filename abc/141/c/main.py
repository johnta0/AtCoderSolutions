N, K, Q = map(int, input().split())
A = []
for _ in range(Q): A.append(int(input()))

points = [K] * N
points = list(map(lambda x: x - Q, points))
for a in A:
    points[a - 1] += 1

# output: 0 opint => No, else => Yes
for p in points:
    if p > 0:
        print('Yes')
    else:
        print('No')
