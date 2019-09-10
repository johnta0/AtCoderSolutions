n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(n):
    if i + 1 == a[i]: continue
    count += 1

if count < 3:
    print("YES")
else:
    print("NO")
