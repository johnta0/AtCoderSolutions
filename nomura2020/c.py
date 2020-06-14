N = int(input())
A = list(map(int, input().split()))

def appropriate(arr):
    for i in range(len(arr) - 1):
        if A[i] > A[i + 1] and A[i] != 0:
            return False
    return True

if not appropriate(A):
    print(-1)
    exit()

A_rev = A[::-1]
cnt = 0
cnt += A[0]
prev = [0]
for i in range(1, N + 1):
    if A[i] == 0:
        cnt += prev
    
