#import numpy as np

def main():
    L, R = list(map(int, input().split()))
    minmod = 10000000
    for i in range(L, R):
        for j in range(i+1, R+1):
            prod = i * j
            mod = prod % 2019
            #mod = np.mod([prod], 2019)[0]
            if mod < minmod:
                minmod = mod
            if minmod < 1:
                break
        else: continue
        break
    print(minmod)

main()
