#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###################
# usage: ./run_length.py aaabbbbbcccdddefffggggg
###################
import sys

# 引数を配列に格納
num = sys.argv[1]

# 変数初期化
count = 1
result = ''

# 配列全体のループ
for i in range(len(num)):
    try:
        if num[i] == num[i+1]:
           count = count + 1
        else:
            result = result + str(num[i]) + str(count)
            count = 1
    except:
        # 最後の文字セットがOutOfRangeになるので結果に出力
        result = result + str(num[i]) + str(count)
        
# 結果をprint
print(result)