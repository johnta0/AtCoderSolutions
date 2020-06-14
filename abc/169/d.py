N = int(input())

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


if N < 2:
    print(0)
    exit()

prime_fct_arr = factorization(N)
ans = 0
for pair in prime_fct_arr:
    e = pair[1]
    e_cur = 0
    while True:
        if e == e_cur or e == 0:
            break
        e_cur += 1
        e -= e_cur
    ans += e_cur
print(ans)
