flatten_A = []

for i in range(3):
    flatten_A.append(list(map(int, input().split())))

N = int(input())
B = [0] * N
for i in range(N):
    B[i] = int(input())

# input ここまで
import itertools
def flatten_list(l):
    return list(itertools.chain.from_iterable(l))

mark_list = [False] * 9

flatten_A = flatten_list(flatten_A)
for b in B:
    if not b in flatten_A: continue
    # 選ばれた数が自分のビンゴに含まれている
    for i in range(9):
        if flatten_A[i] == b:
            mark_list[i] = True

"""
[0, 1, 2], [3, 4, 5], [6, 7, 8]
[0, 3, 6], [1, 4, 7], [2, 5, 8]
[0, 4, 8], [2, 4, 6]
"""
def judge_bingo(l):
    yes = "Yes"
    no = "No"
    if l.count(True) < 3:
        return no
    if l[0]:
        if (l[1] and l[2]) or (l[3] and l[6]) or (l[4] and l[8]):
            return yes
    if l[3] and l[4] and l[5]:
        return yes
    if l[1] and l[4] and l[7]:
        return yes
    if l[2]:
        if l[4] and l[6]: return yes
        if l[5] and l[8]: return yes
    if l[6] and l[7] and l[8]:
        return yes
    return no
        

ans = judge_bingo(mark_list)
print(ans)
# print(A)
# print(flatten_A)
# print(mark_list)
