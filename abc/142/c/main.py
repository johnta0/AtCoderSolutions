N = int(input())
A = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[i] = A[i]
dic_swap = {v: k for k, v in dic.items()}
dic_swap_sorted = sorted(dic_swap.items())

order = []
for tap in dic_swap_sorted:
    order.append(tap[1] + 1)

print(*order)
