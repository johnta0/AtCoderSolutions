a, b, n = map(int, input().split())

def f(x):
    return a * x // b - a * (x // b)

ans = f(min(b - 1, n))
print(ans)
