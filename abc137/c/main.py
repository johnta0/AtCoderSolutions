import itertools

def comb(n, r):
    return len(list(itertools.combinations(range(n), r)))

def get_runlength(s): # ex) s = 'RRLLLLRLRLRLRR'
    ret = []
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            ret.append((s[i], count))
            continue
        if s[i] == s[i + 1]:
            count += 1
        else:
            ret.append((s[i], count))
            count = 1
    return ret

n = int(input())
s = []
for i in range(n):
    sin = input()
    sin = list(sin)
    sin.sort()
    sin = ''.join(sin)
    s.append(sin)

ss = set(s)
count = 0
for u in ss:
    al = s.count(u)
    # s.remove
    count += comb(al, 2)
print(count)