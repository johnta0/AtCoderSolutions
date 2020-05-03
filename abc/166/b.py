N, K = map(int, input().split())
d = []
A = [[] for _ in range(K)]
for i in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))

import itertools
a_flattened = list(itertools.chain.from_iterable(A))
se = set(a_flattened)
print(N - len(se))
