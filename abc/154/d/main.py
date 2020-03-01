N, K = map(int, input().split())
p = list(map(int, input().split()))

MAX = 0
# dp[i] i 番目から i + K - 1 番目までのサイコロの期待値の和
dp = [0] * N
for i in range(N - K + 1):
    if i < 1:
        dp[i] = 0.5 * (sum(p[:K]) + K)
    else:
        dp[i] = dp[i - 1] - 0.5 * p[i - 1] + 0.5 * p[i + K - 1]

    MAX = max(MAX, dp[i])
print(MAX)