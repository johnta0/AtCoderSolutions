def is_num(x):
    try:
        num = int(x)
    except:
        return 'error'
    return 2 * num

print(is_num(input()))