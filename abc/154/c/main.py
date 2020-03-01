N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

def solution(N, A):
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            return "NO"
    return "YES"

print(solution(N, A))
