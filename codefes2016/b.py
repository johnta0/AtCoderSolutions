"""
    参加: N 人
    

    input:
        - S: S[i] == 'a' -> 国内, b -> 海外, c -> Neither
    output: 予選通過/No Yes/No
"""

N, A, B = map(int, input().split())
S = input()

passed_cnt = 0
overseas_cnt = 0
for c in S:
    if c == 'a': # 国内学生
        if passed_cnt < A + B:
            print('Yes')
            passed_cnt += 1
        else:
            print('No')
    elif c == 'b': # 海外学生
        if passed_cnt < A + B and overseas_cnt < B:
            print('Yes')
            passed_cnt += 1
        else:
            print('No')
        overseas_cnt += 1
    else: # 学生でない
        print('No')

