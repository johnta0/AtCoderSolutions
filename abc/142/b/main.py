n, k = map(int, input().split())
H = list(map(int, input().split()))

ppl = 0
for i in range(n):
    if H[i] >= k: ppl += 1
print(ppl)
