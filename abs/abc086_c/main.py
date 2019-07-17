# -*- coding: utf-8 -*-

import numpy as np

"""
    dept_pos: 出発座標
    dest_pos: 到着座標
"""


def is_possible(time_diff, dept_pos, dest_pos):

    pos_diff = np.array(dest_pos) - np.array(dept_pos)
    if abs(pos_diff[0]) + abs(pos_diff[1]) > time_diff:
        return False
    if not (time_diff % 2 == pos_diff[0] + pos_diff[1] % 2):
        return False
    return True

def print_list(list):
    for e in list:
        print(e)

def main():
    N = int(input())
    T = [0]
    X = [0]
    Y = [0]
    for i in range(1, N+1):
        t, x, y = list(map(int, input().split()))
        T.append(t)
        X.append(x)
        Y.append(y)

    for i, t in enumerate(T):
        if i > N - 1:
            break
        if not is_possible(T[i+1] - t, [X[i], Y[i]], [X[i+1], Y[i+1]]):
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
