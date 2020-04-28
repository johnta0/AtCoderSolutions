
# def is_prime(n):


def create_prime_list(n):
    prime_list = [i for i in range(2, n - 1)]
    cnt = 0
    while True:
        p = prime_list[cnt]
        for i in range(len(prime_list)):
            num = prime_list[i]
            if num == p: continue
            if num % p == 0:
                prime_list.pop(i)
    return prime_list

n = 2
while n < 100:
    # n が素数かどうか
    prime_list = create_prime_list(n)
    is_prime = True
    for a in prime_list:
        if n % a == 0:
            is_prime = False
            break
    if is_prime: print(n)
    
    n += 1
