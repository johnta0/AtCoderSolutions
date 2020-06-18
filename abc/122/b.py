s = input()
# ans = 0
# DNA = ['A', 'C', 'G', 'T']
# count = 0
# for i in range(len(s)):
#     c = s[i]
#     if c in DNA:
#         count += 1
#     else:
#         ans = max(ans, count)
#         count = 0
#     if i == len(s) - 1:
#         ans = max(ans, count)
# print(ans)

N = len(s)
ans = 0
for i in range(N):
    for j in range(i, N):
        # if all(c in ['A', 'G', 'C', 'T'] for c in s[i : j + 1]):
        if all('ACGT'.count(c) for c in s[i : j + 1]):
            ans = max(ans, j - i + 1)
print(ans)