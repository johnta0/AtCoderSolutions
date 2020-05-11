import sys

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

N, K = inp_list()
A = inp_list()
A = list(map(lambda x: x - 1, A)) # 0-indexed



pos = 0 # 現在の位置を表す index
# memo = [[False, 0] for _ in range(N)] # memo[i]: [bool, tel_cnt] , [数えたか、何回移動したか]
# memo[0] = [True, 0]
visited = [False for _ in range(N)]
teleport_count = {}
distance = 0
l_pos = 0
tel_cnt = 0
while True:
    nxt = A[pos]
    # if memo[nxt][0]: # 数えた
    if visited[nxt]:
        # r_pos, l_pos = memo[pos][1], memo[nxt][1]
        r_pos, l_pos = teleport_count[pos], teleport_count[nxt]
        distance = r_pos - l_pos
        break
    tel_cnt += 1
    # memo[nxt][1] = tel_cnt
    teleport_count[nxt] = tel_cnt
    # memo[nxt][0] = True
    visited[nxt] = True
    # index 更新
    pos = nxt

def get_key_from_value(val, d):
    for k, v in d.items():
        if v == val:
            return k
# def find_idx_by_telcnt(tel_cnt):
#     for i in range(N):
#         m = memo[i]
#         if m[1] == tel_cnt:
#             return i

if K <= l_pos:
    # print(find_idx_by_telcnt(K) + 1)
    print(get_key_from_value(K, teleport_count) + 1)
else:
    diff = K - l_pos
    rem = diff % (distance + 1)
    ans_pos = l_pos + rem
    # print(find_idx_by_telcnt(ans_pos) + 1)
    print(get_key_from_value(ans_pos, teleport_count) + 1)
