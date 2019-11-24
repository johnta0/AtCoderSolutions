N = int(input())
S = input()

if N % 2 != 0:
    print("No")
else:
    # print(S[:2])
    # print(S[:int(N/2)])
    if S[:int(N/2)] == S[int(N/2):]:
        print("Yes")
    else:
        print("No")