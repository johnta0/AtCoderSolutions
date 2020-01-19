N, K, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) + K < M * N:
    print(-1)
else:
    print(max(M * N - sum(A), 0))
