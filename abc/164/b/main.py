A, B, C, D = map(int, input().split())

# 勝つ Yes, 負ける No
while A > 0 and C > 0:
    C -= B
    if C <= 0:
        print('Yes')
        break
    A -= D
    if A <= 0:
        print('No')
        break

