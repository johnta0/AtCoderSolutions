

def generate_prime_list(n):
    li = list(range(2, n))
    pos = 0

def is_prime(n):
    # n が素数である <=> k = 2, ..., n - 1 で n が割り切れない。
    prime_list = generate_prime_list(n)
    for k in prime_list:
        if n % k == 0:
            return False
    return True

if __name__ == "__main__":
    MAX = 100
    num = 2
    # count = 0
    while num <= MAX:
        if is_prime(num):
            print(num)
            # count += 1
        num += 1
    # print(count)