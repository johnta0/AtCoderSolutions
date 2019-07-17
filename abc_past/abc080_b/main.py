def main():
    a, b, c, d = map(int, input().split())
    if a < c:
        if c < b:
            if b < d:
                print(b - c)
            else:
                print(d - c)
        else:  # b < c
            print(0)
    else:  # a > c
        if a < d:
            if d < b:
                print(d - a)
            else:
                print(b - a)
        else:
            print(0)


"""
    以下、エレガントだなと思ったコードたち
"""

"""
    max, min 関数を上手く使っている。if 条件分岐よりは実行速度が遅いが、
    コードがシンプルですごい。
"""
def t_shinobu_solution():
    row = list(map(int, input().split()))
    start = max(row[0], row[2])
    end = min(row[1], row[3])
    ans = max(end-start, 0)
    print(ans)

if __name__ == "__main__":
    main()
