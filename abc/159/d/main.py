N = int(input())
A = list(map(int, input().split()))

counts = {}
for i in range(N):
    a = A[i]
    if a in counts:
        counts[a] += 1
    else:
        counts[a] = 1

# print(counts)

ans_memory = {}
ans_memory_val = {}
for k in range(N):
    if A[k] in ans_memory:
        print(ans_memory[A[k]])
        continue
    if counts[A[k]] in ans_memory_val:
        print(ans_memory_val[counts[A[k]]])
        continue

    counts_tmp = counts.copy()
    counts_tmp[A[k]] -= 1

    # print(counts_tmp)
    ans = 0
    for v in counts_tmp.values():
        ans += v * (v - 1) // 2
    ans_memory[A[k]] = ans
    ans_memory_val[counts[A[k]]] = ans
    print(ans)
