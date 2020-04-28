from collections import deque

S = deque(input())
lenq = int(input())
Q = [input() for _ in range(lenq)]

# len(S) <= 100000
# lenq <= 2 * 10 ** 5

# q == '1' のとき、実際に反転すると O(N)かかるので反転しないで、
# どちらが先頭かだけの情報を持っておく
head = 1 # or -1
for q in Q:
    if q == '1':
        head *= -1
    else:
        _, f, c = q.split()
        if f == '1':
            if head == 1:
                S.appendleft(c)
            else:
                S.append(c)
        else:  # f == '2'
            if head == 1:
                S.append(c)
            else:
                S.appendleft(c)
S = ''.join(list(S))
if head == -1:
    S = S[::-1]
print(S)
