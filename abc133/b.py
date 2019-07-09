#import numpy as np
import math

def main():
    n, d = list(map(int, input().split()))
    X = []
    for i in range(n):
        X.append(list(map(int, input().split())))

    count = 0
    for i in range(n):
        if i == n: break
        for j in range(i+1, n):
            #Xi, Xj = np.array(X[i]), np.array(X[j])
            #diff = Xj - Xi
            #dist = np.linalg.norm(diff)

            dis = get_distance(X[i], X[j], d)
            if dis.is_integer(): count += 1
            #print('distance:', dis)
    print(count)

def get_distance(P1, P2, d):
    s = 0
    for i in range(d):
        s += (P2[i] - P1[i])**2
    return math.sqrt(s)

main()
