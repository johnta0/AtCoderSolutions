N = int(input())
B = list(map(int, input().split()))

A = [0] * N
# min_index = B.index(min(B))

A[0], A[1] = B[0], B[0]
for i in range(N - 1):
    if B[i] < A[i]: A[i] = B[i]
    A[i + 1] = B[i]
print(sum(A))
