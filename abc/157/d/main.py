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

# N: 人数, M: 友人関係の数, K: ブロック関係の数
N, M, K = map(int, input().split())

# A_i, B_i は友達関係, C_i, D_i はブロック関係
friend_rel = []
/
block_rel = []
for _ in range(K): block_rel.append(list(map(int, input().split())))

# main process
"""
    友達候補 (a, b)：
        - a \ne b
        - a, b はブロック関係でない
        - a, b は友達関係でもない
        - 間接的に友達関係である
"""

## DFS/BFS を用いてグループ分け（連結成分）していく手法



