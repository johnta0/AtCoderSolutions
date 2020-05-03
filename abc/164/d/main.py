S = input()[::-1]
N = len(S)

"""
    例： S = '31415926535'
        S[3:8] = '15926535' が 2019 で割り切れるかどうか？
     <=> S[3:-1] - S[8:-1] が 2019 で割り切れるかどうか
     <=> S[3:-1] % 2019 == S[8:-1] % 2019 か
    よって、2019で割ったときの異なるあまりをそれぞれカウントすればよい
"""

mod_cnts = [0] * 2019
mod_cnts[0] = 1 # 累積和のはじめ
current_cusum, ans = 0, 0
# O(N)
d = 1
for s in S:
    current_cusum += int(s) * d
    current_cusum %= 2019
    d = d * 10 % 2019
    mod_cnts[current_cusum] += 1

# O(2019)
for cnt in mod_cnts:
    ans += cnt * (cnt - 1) // 2 # n_C_2 2つ選ぶ組み合わせ

# O(N + 2019)
 
print(ans)
