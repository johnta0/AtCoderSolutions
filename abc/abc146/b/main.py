n = int(input())
s = input()

alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

out = ''
for c in s:
    idx = alphabets.index(c)
    out += alphabets[(idx + n) % 26]

print(out)
