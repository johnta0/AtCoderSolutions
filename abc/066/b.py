S = input()
N = len(S)
for i in range(2, N, 2):
    ans_str = S[:N - i]
    ans = len(ans_str)
    if ans_str[:ans // 2] == ans_str[ans // 2:]:
        print(ans)
        break

