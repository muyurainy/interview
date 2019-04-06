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
    for i in range(0, len(num), 3):
        tmp = (int(num[i])) * 100 + (int(num[i+1])) * 10 + (int(num[i+2]))
        tmp_str = ['0' for _ in range(10)]
        for j in range(10):
            if tmp == 0:
                break
            if tmp&1:
                tmp_str[9-j] = '1'
            tmp >>= 1
        num2 += ''.join(tmp_str)
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
    for i in range(0, len(num3), 5):
        tmp = (int(num3[i])) * 16 + (int(num3[i+1])) * 8 + (int(num3[i+2])) * 4  + (int(num3[i+3])) * 2 + (int(num3[i+4]))
        if tmp <= 9:
            print(chr(ord('0') + tmp), end='')
        else:
            print(chr(ord('A') + tmp - 10) , end ='')
    print('')