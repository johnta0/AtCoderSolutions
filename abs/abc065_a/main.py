
def yes():
    print("YES")

def no():
    print("NO")

def main():
    # words = ['dream', 'dreamer', 'erase', 'eraser']
    s = input()

    """  fastest and the most elegant code """
    # rep = s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
    # if not rep:
    #     print('YES')
    # else:
    #     print("NO")

    if len(s) < 5:
        no()
        return

    s = s[::-1]
    pos = 0
    while pos < len(s):
        if s[pos:pos + 5] == 'dream'[::-1] or s[pos:pos + 5] == 'erase'[::-1]:
            pos += 5
        elif s[pos:pos + 6] == 'eraser'[::-1]:
            pos += 6
        elif s[pos:pos + 7] == 'dreamer'[::-1]:
            pos += 7
        else:
            no()
            return
        

    """
        以下のコードは、S = "eraseraseraseraseraseraseraser" のように、区切る場所が最後まで定まらない場合には計算量が多くなる。
    """
    # pos = 0
    # while pos < len(s):
    #     if (s[pos:pos+5] != "dream") and (s[pos:pos+5] != "erase"):
    #         no()
    #         return

    #     if s[pos:pos+5] == "dream":
    #         if s[pos:pos + 7] == "dreamer":
    #             if s[pos + 5:pos + 11] != "eraser":
    #                 pos += 11
    #             elif s[pos + 5:pos + 10 != "erase"]:
    #                 if s[pos]
    #             else:
    #                 pos += 7
    #         else:
    #             pos += 5
    #     elif s[pos:pos + 5] == "erase":
    #         if s[pos:pos + 6] == "eraser":
    #             pos += 6
    #         else:
    #             pos += 5
    yes()
    
if __name__ == "__main__":
    main()
