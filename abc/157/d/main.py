# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n # size of union find
        self.parents = [-1] * n

    # root を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # グループを結合する（２つの要素が同じグループである）
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


# input
N, M, K = map(int, input().split())
# A = [0] * M
# B = [0] * M
# for i in range(M): A[i], B[i] = map(int, input().split())
# C = [0] * K
# D = [0] * K
# for i in range(K): C[i], D[i] = map(int, input().split())

uf = UnionFind(N)

f_relation = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    f_relation[a - 1].append(b - 1)
    f_relation[b - 1].append(a - 1)
    uf.unite(a - 1, b - 1)

b_relation = [[] for _ in range(N)]
for _ in range(K):
    c, d = map(int, input().split())
    b_relation[c - 1].append(d - 1)
    b_relation[d - 1].append(c - 1)

# ans: 1, 2, ..., N の人それぞれに対して、友達候補の数
ans = [0 for _ in range(N)]
for i in range(N):
    # i の友達候補（ブロックは考えない） = i と同じグループ（間接的でもつながっている） - 

# main process

"""
    友達候補 (a, b)：
        - a \ne b
        - a, b はブロック関係でない
        - a, b は友達関係でもない
        - 間接的に友達関係である
"""


