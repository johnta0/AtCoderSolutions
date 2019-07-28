n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s1 = sum(a)
for i in range(n + 1):
    if i == 0:
        if a[i] < b[i]:
            b[i] -= a[i]
            a[i] = 0
        else:
            a[i] -= b[i]
            b[i] = 0
    elif i == n:
        if a[i] < b[i - 1]:
            a[i] = 0
        else:
            a[i] -= b[i - 1]
            b[i - 1] = 0
    else:
        if a[i] < b[i - 1]:
            a[i] = 0
        else:
            a[i] -= b[i - 1]
        if a[i] < b[i]:
            b[i] -= a[i]
            a[i] = 0
        else:
            a[i] -= b[i]
            b[i] = 0
print(s1 - sum(a))
