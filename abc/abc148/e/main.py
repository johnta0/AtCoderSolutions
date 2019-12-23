n = int(input())

if n % 2 != 0:
    print(0) # 奇数は10が現れない
else:
    s = str(n)
    m = len(s)  # 桁数
    for j in range(m)[::-1]:
        n_ = int(s[0 : j-1] + )
