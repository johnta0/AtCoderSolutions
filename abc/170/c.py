X, N = map(int, input().split())
pp = list(map(int, input().split()))
pp.sort()

if N == 0:
    print(X)
    exit()
if X not in pp:
    print(X)
    exit()

ans = X
diff = 0
while True:
    diff += 1
    ans = X - diff
    if ans not in pp:
        print(ans)
        break
    ans = X + diff
    if ans not in pp:
        print(ans)
        break

# left, right = 0, 0
# for i in range(N):
#     if i == N - 1:
#         left, right = , -1
#     if pp[i] == X:
#         cur = i
#         break
#     if pp[i] > X:
#         if i == 0:
#             left, right = -1, pp[i]
#         else:
#             left, right = pp[i - 1], pp[i]

#         break


