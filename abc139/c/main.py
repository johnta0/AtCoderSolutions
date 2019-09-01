N = int(input())
H = list(map(int, input().split()))

maximum = 0
pos = -1
for i in range(N - 1):
    if H[i] < H[i + 1]:
        maximum = max(maximum, i - pos - 1)
        pos = i
# print(pos)
maximum = max(maximum, (N - 1) - pos - 1)
print(maximum)
