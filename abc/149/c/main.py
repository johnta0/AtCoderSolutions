def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1
