N = int(input())
for x in range(1, 50000):
    if int(x * 1.08) == N:
        print(x)
        exit()
print(":(")
