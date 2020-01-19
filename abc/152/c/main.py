N = int(input())
P = list(map(int, input().split()))

count = 1
mini = P[0]
for i in range(1, N):
    mini = min(mini, P[i])
    if P[i] <= mini:
        count += 1

print(count)