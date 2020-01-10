s = input()

ite = 0
if len(s) % 2 == 0:
    ite = int(len(s) / 2)
else:
    ite = int((len(s) - 1) / 2)

count = 0
for i in range(ite):
    if s[i] == s[-i - 1]:
        continue
    count += 1

print(count)