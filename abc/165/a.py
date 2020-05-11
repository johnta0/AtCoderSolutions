k = int(input())
a, b = map(int, input().split())
for num in range(k, 1001, k):
    if a <= num <= b:
        print('OK')
        exit()
print('NG')
