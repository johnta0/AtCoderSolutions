n = int(input())
a = list(map(int, input().split()))

counter = 1
for i in range(n):
    if a[i] == counter:
        counter += 1
if counter == 1:
    print(-1)
else:
    print(n - counter + 1)
