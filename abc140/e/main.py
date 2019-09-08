n = int(input())
p = list(map(int, input().split()))

s = 0
for i in range(N - 1):
    plr = p[i : i + 1]
    plr.sort()
    plr = plr[-2:]
    s += plr[0]
    for j in range(i + 1, N):
        plr.append(p[])
