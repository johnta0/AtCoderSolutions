K = int(input())
cnt = 0

def is_runrun(num):
    s = str(num)
    is_runrun = True
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) > 1:
            is_runrun = False
            break
    return is_runrun, idx

pos = 1
prev_runrun = False
while True:
    # s = str(pos)
    # is_runrun = True
    # for i in range(len(s) - 1):
    #     if abs(int(s[i]) - int(s[i + 1])) > 1:
    #         is_runrun = False
    #         break

    s = str(pos)
    li = list(s)
    li = list(map(int, li))

    # if len(s) > 3 and abs(int(s[0]) - int(s[1])) > 1:
    #     if s[0] == '9':
    #         pos = int('1' + '0' * len(s))
    #         continue
    #     if s[1] == '9':
    #         pos = int(str(int(s[0]) + 1) + '0' * (len(s) - 1))
    #         continue
    #     pos = s[0] + str(int(s[1]) + 1) + '0' * 

    # もし, 18xxx のように8xxxの台にルンルン数がないような pos の場合、125x
    isrunurn, idx = is_runrun()
    if isrunrun:
        cnt += 1
        if cnt == K: break
    else:
        if li[idx] < 9:
            pos = li[:idx] + s[idx] + s[idx + 1] +
            li[idx + 1] += 1
        else: # li[idx] == 9
            if idx == 0:
                pass
            else:
                li[idx] = 0
                for 

                idx[idx + 1] = 0
    pos += 1

print(pos)
