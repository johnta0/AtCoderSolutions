n = int(input())
pp = list(map(int, input().split()))

# flag = True # p(i) が p(i-1) より大きいか小さいかのフラグ
count = 0
for i in range(1, n - 1):
    partial = sorted(pp[i - 1:i + 2])
    if partial[1] == pp[i]:
        count += 1

print(count)
