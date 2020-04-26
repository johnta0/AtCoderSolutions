N = int(input())
# aa = []
# for _ in range(N): aa.append(int(input()))
aa = [int(input()) for _ in range(N)]

"""
    条件
        - はじめ、ボタン1が光っている
        - ボタン2が光っている状態で終了したい
        - そのようなことは可能か？可能ならボタンを押す最低回数を、不可能なら-1を出力せよ。
"""

ans = -1
cnt = 0
pos = 0
for _ in range(N): # N回ボタンを押す
    cnt += 1
    pos = aa[pos] - 1
    if pos == 1:
        ans = cnt
        break

print(ans)
