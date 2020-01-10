def win_rsp(hand):
    if hand == 'r':
        return 'p'
    elif hand == 's':
        return 'r'
    else:  # 'p'
        return 's'


N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

get_score = {'r': R, 's': S, 'p': P}

player_hands = [''] * N
score = 0
# for i in range(N):
#     if player_hands[i] != '':
#         continue
#     if i > K - 1:  # K 回前と同じ手は出せない
#         for j in range(i, N, K):
#             if player_hands[j] != '':
#                 continue
#             if win_rsp(T[j]) == player_hands[j - K]:  # 勝てない
#                 player_hands[j] = 'X'  # 残りふたつのどちらか
#                 player_hands[j + K] = win_rsp[T[j + K]] # j + K 回目で勝つしか無い
#                 # add score
#                 score += get_score[player_hands[j + K]]

#     else:  # ただ勝てばいい
#         player_hands[i] = win_rsp(T[i])
#         # add score
#         score += get_score[player_hands[i]]

t = list(T)
# print(t)
for i in range(K):
    spl = t[i::K]
    win_l = list(map(win_rsp, spl))
    # print(win_l)
    # for i in range(len(win_l)):
    j = 0
    while j < len(win_l):
        if j == len(win_l) - 1:
            score += get_score[win_l[j]]
            # print(get_score[win_l[j]])
            # print('score:', score)
            break
        if win_l[j] != win_l[j + 1]:
            score += get_score[win_l[j]]
            # print(get_score[win_l[j]])
            # print('score:', score)
            j += 1
        else:
            score += get_score[win_l[j]]
            # print(get_score[win_l[j]])
            j += 2

    # print(spl)
    # odd_l = spl[::2]
    # eve_l = spl[1::2]
    # print(odd_l)
    # print(eve_l)

    # win_odd_l = list(map(win_rsp, odd_l))
    # win_eve_l = list(map(win_rsp, eve_l))
    # print('win_odd_l', win_odd_l)
    # print('win_eve_l', win_eve_l)

    # odd_score = 0
    # eve_score = 0
    # for o in win_odd_l:
    #     odd_score += get_score[o]
    # for e in win_eve_l:
    #     eve_score += get_score[e]

    # m = max(odd_score, eve_score)
    # print(m)
    # score += m

print(score)
