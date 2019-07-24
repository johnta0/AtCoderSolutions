n = int(input())
a = list(map(int, input().split()))

b = [0] * n
for i in range(n)[::-1]:
    multiple = b[i::i + 1]
    if sum(multiple) % 2 != a[i]:  # 偶奇が一致していない場合
        b[i] = 1  # ボールを入れる
    
print(sum(b))
true_b = []  # ボールが入っている箱の番号 true_b
for i in range(n):
    if b[i] == 0: continue
    true_b.append(str(i + 1))

if len(true_b) != 0:
    print(' '.join(true_b))
