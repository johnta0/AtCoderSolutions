A, B = input().split()
A = int(A)
# B = int(B.replace('.', ''))
B = float(B)
B = int(B * 100 + 2 ** (-6))
ans = A * B // 100
print(ans)
