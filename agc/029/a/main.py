S = input() # S_i = B(lack) or W(hite)
N = len(S)

"""
    最終的には W..W...B...B のような並びになる。
    元の状態から B がどれだけ右に進んだかの総和が答え。
"""

def sum_contin_int(l, r):
    return (r * (r + 1) - l * (l - 1)) // 2


""" White version """
cnt_initial = 0
cnt_w = 0
for i in range(N):
    if S[i] == 'W':
        cnt_initial += i
        cnt_w += 1
ans = cnt_initial - sum([i for i in range(cnt_w)])

""" Black version """
# cnt_initial = 0
# cnt_b = 0
# for i in range(N):
#     if S[i] == 'B':
#         cnt_initial += i
#         cnt_b += 1

# # cnt_final = sum_contin_int(N - cnt_b, N - 1)
# cnt_final = sum([i for i in range(N - cnt_b, N)])

# ans = cnt_final - cnt_initial
print(ans)