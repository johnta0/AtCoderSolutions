A, B, C = map(int, input().split())

if A == B and B == C:
    print("No")
elif A != B and B != C and C != A:
    print("No")
else:
    print("Yes")
