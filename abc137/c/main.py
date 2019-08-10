import itertools

n = int(input())
dic = {}
for i in range(n):
    sin = input()
    sin = list(sin)
    sin.sort()
    sin = ''.join(sin)
    try:
        dic[sin] += 1
    except:
        dic[sin] = 1

count = 0
for v in dic.values():
    count += v * (v - 1) / 2
count = int(count)
print(count)