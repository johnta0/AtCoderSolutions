N, M, S = map(int, input().split())

U = [0] * M
V = [0] * M
A = [0] * M
B = [0] * M
for i in range(M):
    U[i], V[i], A[i], B[i] = map(int, input().split())

C = [0] * N
D = [0] * N
for i in range(N):
    C[i], D[i] = map(int, input().split())


