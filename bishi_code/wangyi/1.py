    '''扑克牌A~K, 给定每种扑克牌的数量，输出顺子的个数（顺子要大于5张）
    输入:
    4
    7
    2
    5
    10

    Notes
    -----
    直接贪心去做, 需要注意这里的小技巧就是sum从0开始，
    而sum_m += mon[m-1-i]
    '''

def str_int(string):
    if string == 'A':
        return 1
    if string == 'J':
        return 11
    if string == 'Q':
        return 12
    if string == 'K':
        return 13
    return int(string)

T = int(input())
for _ in range(T):
    N = int(input())
    string = [0 for _ in range(14)]
    tmp = list(map(str_int, input().split(' ')))
    for i in range(len(tmp)):
        string[tmp[i]] += 1
    res = 0
    tmp = 0
    for i in range(9, 0, -1):
        tmp = tmp * string[i] + string[i]*string[i+1]*string[i+2]*string[i+3]*string[i+4]
        res += tmp
        '''
        if (string[i] == 0):
            tmp = 0
            continue
        if tmp != 0:
            tmp = tmp * string[i] + string[i]*string[i+1]*string[i+2]*string[i+3]*string[i+4]
            res += tmp
        else:
            tmp = string[i] * string[i+1] * string[i+2] * string[i+3] * string[i+4]
            res += tmp
        '''
    print ("{}".format(res))