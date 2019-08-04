s = input()
n = len(s)
ch = [1] * n

for _ in range(10 ** 100):
    tmp = [0] * n
    for i in range(n):
        if i == 0:
            tmp[1] += ch[0]
        elif i == n - 1:
            tmp[n - 2] += ch[n - 1]
        else:
            if s[i] == "R":
                tmp[i + 1] += ch[i]
            else:
                tmp[i - 1] += ch[i]
    ch = tmp

for i in ch:
    print(i + " ")
