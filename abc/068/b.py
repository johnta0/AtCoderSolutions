N = int(input())
n = 0
while True:
    if 2 ** n > N:
        print(2 ** (n - 1))
        break
    n += 1
