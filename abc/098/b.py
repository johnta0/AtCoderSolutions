N = int(input())
S = input()

ans = max(len(set(S[i:]) & set(S[:i])) for i in range(1, N))
print(ans)

# def count_alphabets(s):
#     alphabets = list("abcdefghijklmnopqrstuvwxyz")
#     cnt = dict(zip(alphabets, [0 for _ in range(26)]))
#     for c in s: cnt[c] += 1
#     return cnt

# ans = 0
# for div in range(1, N):
#     left_str, right_str = S[:div], S[div:]
#     left_cnt, right_cnt = count_alphabets(left_str), count_alphabets(right_str)

#     count = 0
#     alphabets = list("abcdefghijklmnopqrstuvwxyz")
#     for c in alphabets:
#         if left_cnt[c] > 0 and right_cnt[c] > 0:
#             count += 1
#     ans = max(ans, count)
# print(ans)
