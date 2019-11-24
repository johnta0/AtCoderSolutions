a, b, x = map(int, input().split())

def d(n):
    return len(str(n))

def find_y(n):
    return a * n + b * d(n)

MAX_N = 10 ** 9

n = 0
if x < 1000:
    while True:
        n += 1
        y = find_y(n)
        if x < y: # 買えない
            n -= 1
            break
else:
    n_approx = int((x - b) / a)  # n はこれより小さい N < X / A
    while True:
        n_approx -= 1
        y = find_y(n_approx)
        if x > y:  # 買える
            n = n_approx

print(n)
