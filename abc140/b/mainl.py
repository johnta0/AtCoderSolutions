N = int(input())
A = list(map(int, input().split())) # length: N
B = list(map(int, input().split())) # length: N
C = list(map(int, input().split())) # length: N - 1

M = 0
M += sum(B)
for i in range(N - 1):
    if A[i + 1] - A[i] == 1:
        M += C[A[i] - 1]

print(M)