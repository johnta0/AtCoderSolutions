N = int(input())
ss = []
for _ in range(N): ss.append(input())

from collections import Counter

ctr = Counter(ss)
counted = ctr.most_common()
# print(counted)
ans = []
for i in range(len(counted)):
    tup = counted[i]
    if i == 0:
        ans.append(tup[0])
        continue
    if counted[i][1] != counted[i - 1][1]:
        break
    ans.append(tup[0])

ans.sort()
for a in ans: print(a)
