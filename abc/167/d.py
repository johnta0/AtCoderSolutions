N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x - 1, A)) # 0-indexed

pos = 0
memo = [[False, 0] for _ in range(N)] # memo[i]: [bool, tel_cnt] , [数えたか、何回移動したか]
memo[0] = [True, 0]
distance = 0
l_pos = 0
tel_cnt = 0
while True:
    next = A[pos]
    tel_cnt += 1
    if memo[next][0]: # 数えた
        r_pos, l_pos = memo[pos][1], memo[next][1]
        distance = r_pos - l_pos
        break
    memo[next][1] = tel_cnt
    memo[next][0] = True
    # index 更新
    pos = next

def find_idx_by_telcnt(tel_cnt):
    for i in range(N):
        m = memo[i]
        if m[1] == tel_cnt:
            return i

if K <= l_pos:
    print(find_idx_by_telcnt(K) + 1)
else:
    diff = K - l_pos
    rem = diff % (distance + 1)
    ans_pos = l_pos + rem
    print(find_idx_by_telcnt(ans_pos) + 1)
