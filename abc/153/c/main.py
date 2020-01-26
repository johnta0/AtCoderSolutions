N, K = map(int, input().split())
H = list(map(int, input().split()))

if N <= K:
    print(0)
else:
    sorted_H = sorted(H, reverse=True)
    ess = sorted_H[K:]
    print(sum(ess))
