s = input()

pos = []
ns = []
for i in range(len(s)):
    if s[i] != '?':
        pos.append(i)
        ns.append(s[i])

MAXIMUM = int(s.replace('?', '9'))
count = 0
num = 13
while num + 5 < MAXIMUM + 1:
    e = str(num + 5)
    for a, b in zip(pos, ns):
        if e[a] == b:
            count += 1

    count %= 10 ** 9 + 7
    num += 13