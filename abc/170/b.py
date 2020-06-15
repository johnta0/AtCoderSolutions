X, Y = map(int, input().split())

if Y % 2 != 0:
    print('No')
elif 4 * X < Y:
    print('No')
elif 2 * X > Y:
    print('No')
else:
    print('Yes')
