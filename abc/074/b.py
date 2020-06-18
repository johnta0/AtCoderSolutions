N = int(input())
K = int(input())
xx = list(map(int, input().split()))

border = K // 2
ans = 0
for x in xx:
    if x <= border:
        # A が動く
        ans += x * 2
    else:
        # B が動く
        ans += (K - x) * 2
print(ans)
