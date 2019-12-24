n = int(input())

ans = "No"
for i in range(1, 10):
    if n == i:
        ans = "Yes"
        break
    if i != 1 and n % i == 0 and n / i < 10:
        ans = "Yes"
        break
print(ans)
