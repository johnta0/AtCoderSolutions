
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

srtd = sorted(A)
for i in range(N):
    # print(str(i) + '番目')
    if srtd[-1] != A[i]:
        print(srtd[-1])
    else:
        print(srtd[-2])
