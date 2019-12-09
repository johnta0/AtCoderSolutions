n = int(input())

a = [0] * n
x = [[0] * n] * n
y = [[0] * n] * n

for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        x[i][j], y[i][j] = map(int, input().split())
