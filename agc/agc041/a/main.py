N, A, B = map(int, input().split())

if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    if N - A > B - 1:  # 1 で対戦
        print(B - 1)
    else:
        print(N - A)
