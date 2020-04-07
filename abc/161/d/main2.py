K = int(input())
li = list(range(1, 10))

while True:
    if K <= len(li):
        print(li)
        print(li[K - 1])
        exit()
    prev_li = list()
    prev_li, li = li, prev_li
    K -= len(li)
    for x in prev_li:
        for i in range(-1, 2):  # 一番右の桁に -1, 0, 1 をくっつけてルンルン数をつくる
            d = x % 10 + i  # 加える桁 d
            if d < 0 or d > 9:
                continue
            next_lunlun = 10 * x + d
            li.append(next_lunlun)
