a, b = map(int, input().split())

tako = 0
outlet = 1
while outlet < b:
    outlet += a - 1
    tako += 1
print(tako)
