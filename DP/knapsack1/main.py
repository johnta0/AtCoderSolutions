import numpy as np

n, C = map(int, input().split())

dp = np.zeros((n + 1, C + 1))
for i in range(1, n + 1):
    w, v = map(int, input().split())
    dp[i] = dp[i - 1]
    
