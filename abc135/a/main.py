a, b = map(int, input().split())
c = a + b
if c % 2 == 1:
    print("IMPOSSIBLE")
else:
    print(int(c / 2))
