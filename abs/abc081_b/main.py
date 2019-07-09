
def main():
    n = int(input())
    lis = list(map(int, input().split()))
    ans = judge(n, lis)
    print(ans)

def judge(n, lis):
    ret = 0
    while True:
        for i in range(n):
            tmp = lis[i]
            if tmp % 2 != 0:
                return ret
            lis[i] = tmp / 2
        ret += 1

if __name__ == '__main__':
    main()

