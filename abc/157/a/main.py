"""
 = int(input())
 = map(int, input().split())
 = list(map(int, input().split()))
"""

N = int(input())
if N % 2 == 0:
    print(N // 2)
else:
    print(N // 2 + 1)

