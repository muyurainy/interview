T = int (input())
for _ in range(T):
    num = input()
    if len(num) % 3 == 1:
        num = '00' + num
    elif len(num) % 3 == 2:
        num = '0' + num
    first = True
    num2 = ''
    tmp = 0
    i = 0
    while(True):
        if i >= len(num):
            break
        tmp = (int(num[i])) * 100 + (int(num[i+1])) * 10 + (int(num[i+2]))
        tmp_str = ['0' for _ in range(10)]
        for j in range(10):
            if tmp == 0:
                break
            if tmp&1:
                tmp_str[9-j] = '1'
            tmp >>= 1
        for s in tmp_str:
            num2 += s
        i += 3
    num3 = ''
    first = True
    for s in num2:
        if first:
            if s == '0':
                continue
            first = False
        num3 += s
    if len(num3) % 5:
        num3 = '0' * (5 - len(num3) % 5) + num3
    i = 0
    while(True):
        if i >= len(num3):
            break
        tmp = (int(num3[i])) * 16 + (int(num3[i+1])) * 8 + (int(num3[i+2])) * 4  + (int(num3[i+3])) * 2 + (int(num3[i+4]))
        if tmp <= 9:
            print(str(tmp), end='')
        else:
            print(chr(ord('A') + tmp - 10) , end = '')
        i += 5
    print('')