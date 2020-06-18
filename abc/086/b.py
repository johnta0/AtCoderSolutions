a, b = input().split()
num = int(a + b)
heihosu = []
for i in range(4, 1000):
    heihosu.append(i * i)
# print(heihosu)
if num in heihosu:
    print('Yes')
else:
    print('No')
