N, M = map(int, input().split())
s = [0] * M
c = [0] * M
for i in range(M):
    s[i], c[i] = map(int, input().split())

"""
    - s, c = (3, 4) かつ s, c = (3, 5) のように、矛盾していたら return -1
    - 
"""

def get_index(l, e):
    return [i for i, x in enumerate(l) if x == e]

def solve(N, M, s, c):
    if M == 0:
        if N == 1:
            return 0
        elif N == 2:
            return 10
        else:
            return 100

    indices_1 = get_index(s, 1)

    for index_1 in indices_1:
        if c[index_1] == 0 and N > 1:
            return -1

    """
        s, c = (3, 4) かつ s, c = (3, 5) のように、矛盾していたら return -1
    """

    z = zip(s, c)
    z = sorted(z)
    s, c = zip(*z)

    if N == 2:
        ans_l = [-1, -1]
    elif N == 3:
        ans_l = [-1, -1, -1]

    for i in range(M):
        if i > 0 and s[i] == s[i - 1]:
            if c[i] == c[i - 1]: continue
            return -1
        if N == 1:
            return c[i]
        ans_l[s[i]] = c[i]
        
    if N == 2:
        if ans_l[0] != -1 and ans_l[0] != -1:
            ans_l = list(map(str, ans_l))
            return int(''.join(ans_l))
        elif ans_l[0] == -1:
            return int('1' + str(ans_l[1]))
        elif ans_l[1] == -1:
            return int(str(ans_l[0]) + '0')
    elif N == 3:
        if ans_l[0] != -1 and ans_l[1] != -1 and ans_l[2] != -1:
            ans_l = list(map(str, ans_l))
            return int(''.join(ans_l))

        

    
            
        



print(solve(N, M, s, c))
