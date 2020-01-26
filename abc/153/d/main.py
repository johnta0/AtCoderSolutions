H = int(input())

count = 1
while True:
    if not H > 1:
        break
    H = H // 2
    count += 1

ans = 2 ** count - 1
print(ans)
