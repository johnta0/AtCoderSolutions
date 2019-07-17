import numpy as np

def main():
    H, W = map(int, input().split())
    s = [input() for i in range(H)]
    
    diffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for y in range(H):
        anstr = ''
        for x in range(W):
            if s[y][x] == '#':
                anstr += '#'
                continue
            count = 0
            for dx, dy in diffs:
                if (x + dx < 0) or (x + dx > W - 1) or (y + dy < 0) or (y + dy > H - 1):
                    continue
                if s[y + dy][x + dx] == '#':
                    count += 1
            anstr += str(count)
        print(anstr)
    
if __name__ == "__main__":
    main()