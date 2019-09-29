n = int(input())
if n % 2 == 0: print(0.5)
elif n == 1: print(1.0)
else:
    odd = (n - 1) / 2 + 1
    print(odd / n)
