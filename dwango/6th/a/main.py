n = int(input())
s = [''] * n
t = [0] * n
for i in range(n):
    s[i], t_i = input().split()
    t[i] = int(t_i)
X = input()

print(sum(t[s.index(X) + 1:]))
