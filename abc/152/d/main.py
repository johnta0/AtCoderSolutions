N = int(input())

pairs = [[0] * 10 for _ in range(10)]
for i in range(1, N + 1):
    s = str(i)
    a, b = int(s[0]), int(s[-1])
    pairs[a][b] += 1

count = 0
for i in range(1, N + 1):
    s = str(i)
    a, b = int(s[0]), int(s[-1])
    count += pairs[b][a]

# print(pairs)
print(count)
