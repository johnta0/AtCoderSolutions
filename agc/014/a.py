A, B, C = map(int, input().split())


count = 0
while True:
    if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
        print(count)
        break
    if A == B == C:
        print(-1)
        break
    A, B, C = B // 2 + C // 2, A // 2 + C // 2, A // 2 + B // 2
    count += 1
