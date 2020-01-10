a = list(map(int, input().split()))
s = sum(a)
if s > 21:
    print('bust')
else:
    print('win')
