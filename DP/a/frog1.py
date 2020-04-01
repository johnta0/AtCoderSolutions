N = int(input())
h = [i for i in map(int, input().split())]

"""
    dp値を書き込んでいく。
    dp値はこの場合、その足場にたどり着くまでの最小コストのことである。
"""
dp = [0] * N
# 0番目でのコストは0なので dp[0] = 0
# 1番目でのコストは0番目から1つ飛ぶ場合の一通り。0と1番目の高さの差を代入
dp[1] = abs(h[0] - h[1])
# 2番目以降は、1つ前と2つ前から飛ぶ場合があるのでイテレーションする
for i in range(2, N):
    dp[i] = min(
        dp[i - 2] + abs(h[i] - h[i - 2]),
        dp[i - 1] + abs(h[i] - h[i - 1]),
        )
print(dp[N - 1])

# submission: https://atcoder.jp/contests/dp/submissions/6842867