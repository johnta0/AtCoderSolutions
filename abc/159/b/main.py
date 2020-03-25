S = input()
N = len(S)

if S[::-1] != S:
    print("No")
    exit()

ss = S[:(N - 1) // 2]
# print(ss)
if ss[::-1] != ss:
    print("No")
    exit()

sss = S[(N + 3) // 2 - 1:]
# print(sss)
if sss[::-1] != sss:
    print("No")
    exit()

print("Yes")
