N = int(input())
S = [''] * N
for i in range(N):
    S[i] = input()

words = []
nums = []
for i in range(N):
    if S[i] not in words:
        words += S[i]
        nums += 1
    else:
        nunms[words.index(S[i])] += 1

for w in max_k_list:
    print(w)

