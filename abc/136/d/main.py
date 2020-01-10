import math

def get_runlength(s): # ex) s = 'RRLLLLRLRLRLRR'
    ret = []
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            ret.append((s[i], count))
            continue
        if s[i] == s[i + 1]:
            count += 1
        else:
            ret.append((s[i], count))
            count = 1
    return ret

s = input()
n = len(s)
ch = [1] * n

# 以下だと時間計算量がO(N^2)になってしまう。
# for _ in range(10 ** 100):
#     tmp = [0] * n
#     for i in range(n):
#         if i == 0:
#             tmp[1] += ch[0]
#         elif i == n - 1:
#             tmp[n - 2] += ch[n - 1]
#         else:
#             if s[i] == "R":
#                 tmp[i + 1] += ch[i]
#             else:
#                 tmp[i - 1] += ch[i]
#     ch = tmp

# for i in ch:
#     print(i + " ")

"""
    10^100 回移動を行うということは、すなわち「十分な回数」「偶数回」移動をする
    ということである。
    文字列を
    RR...RLL...L の塊の分解することができる。たとえば

    RRLRL は RRL と RL に分解でき、十分な移動のあとはそれらの境界 LR の間を行き来する。
    また、偶数回の移動後、子どもたちがいるマスははじめ子どもたちがいたマスの偶奇と一致する。
    それを利用して実装していく

    例: RRLLLLRLRRLL
"""
# 最終的なこどもたちの数
ch = [0] * len(s)
# runlength を計算
rl = get_runlength(s)

i = 0
pos = 0
while i < len(rl):
    r, l = rl[i], rl[i + 1]
    # R の右端
    ch[pos + r[1] - 1] = math.floor(l[1] / 2) + math.floor((r[1] + 1) / 2)
    # L の左端
    ch[pos + r[1]] = math.floor(r[1] / 2) + math.floor((l[1] + 1) / 2)
    i += 2
    pos += r[1] + l[1]

print(' '.join(map(str, ch)))
