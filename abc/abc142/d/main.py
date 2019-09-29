def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())

a_divsrs = set(make_divisors(a))
b_divsrs = set(make_divisors(b))

# print("a_divsrs:", *a_divsrs)
# print("b_divsrs:", *b_divsrs)

comm_divsrs = sorted(a_divsrs & b_divsrs)

# print("comm_divsrs:", *comm_divsrs)

ans = []
for i in range(len(comm_divsrs)):
    if not (comm_divsrs[i] % 2 == 0 and comm_divsrs[i] != 2):
        ans.append(comm_divsrs[i])

# print("ans:", *ans)

final_ans = ans[0:2]
# ct = 0

"""
    ans[i] に対して、すべての ans[j] (j: range[1:i]) が gcd(ans[i], ans[j]) == 1
    ならば final_ans に追加。ひとつでも違えば追加しない
"""
for i in range(2, len(ans)):
    is_ok = True
    for j in range(1, i):
        if gcd(ans[i], ans[j]) != 1:
            is_ok = False
            break
    if is_ok:
        final_ans.append(ans[i])

# print("final_ans:", *final_ans)
print(len(final_ans))
# print(ct)
