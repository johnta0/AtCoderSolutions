N, M = map(int, input().split())
p = [0] * M
S = [''] * M
for i in range(M):
    p_i, S[i] = input().split()
    p[i] = int(p_i)

penal_ct = 0
ac_count = 0
# prev_ac_num = -1
ac_list = [False] * N
pos = 0

wa_count = [0] * N

for i in range(M):
    if S[i] == 'WA':
        wa_count[p[i] - 1] += 1
        # print(wa_count[p[i] - 1])
    elif (not ac_list[p[i] - 1]) and S[i] == 'AC': # ACかつ今までにACしてない
        ac_list[p[i] - 1] = True
        ac_count += 1
        if i == 0:
            continue
        penal_ct += wa_count[p[i] - 1]
        # for j in range(i)[::-1]:
        #     if S[j] == 'WA' and p[j] == p[i]:
        #         penal_ct += 1
    # if all(ac_list):
        # break
# print(wa_count)
print(ac_count, penal_ct) 
