A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

d = abs(A - B)
if (V - W) * T >= d:
    print('YES')
else:
    print('NO')
