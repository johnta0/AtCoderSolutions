N, M = map(int, input().split())
H = list(map(int, input().split()))
groups = [[] for _ in range(N)]
for i in range(N):
    groups[i].append(H[i])

for _ in range(M):
    a, b = map(int, input().split())
    groups[a - 1].append(H[b - 1])
    groups[b - 1].append(H[a - 1])

ans = 0
for i in range(N):
    g = groups[i]
    g.sort(reverse=True)
    if len(g) == 1:
        ans += 1
        continue
    if g[0] != g[1] and g[0] == H[i]:
        ans += 1
print(ans)

