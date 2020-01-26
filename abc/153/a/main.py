H, A = map(int, input().split())
ans = H // A + 1

if H % A == 0:
    print(ans - 1)
else:
    print(ans)
