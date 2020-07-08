n = int(input())
pay = 1000
while True:
    if pay < n:
        pay += 1000
        continue
    print(pay - n)
    break
