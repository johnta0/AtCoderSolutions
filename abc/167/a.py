s = input()
t = input()

if s == t[:-1] and len(t) - len(s) == 1:
    print('Yes')
else:
    print('No')
