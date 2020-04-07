N = int(input())
X = list(map(int, input().split()))

"""
    min(X) 以上、 max(X) 以下の整数を全探索
    1 <= X[i] <= 100 なので時間計算量は O(N(Xmax - Xmin)) <= O(N^2)
"""

X.sort()
ans = 10 ** 12
for p in range(X[0], X[N - 1] + 1):
    total = 0
    for x in X:
        total += (x - p)** 2
    ans = min(ans, total)
print(ans)
