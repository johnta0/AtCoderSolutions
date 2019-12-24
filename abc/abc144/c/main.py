n = int(input())

ans = 10**12
for i in range(1, int(n ** 0.5) + 1):
    if n % i != 0:
        continue
    move = i + int(n / i) - 2
    if move < ans:
        ans = move
print(ans)
