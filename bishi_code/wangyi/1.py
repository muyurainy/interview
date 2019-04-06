
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
    #string = list(map(str_int, input().split(' ')))
    #string = sorted(string)
    string = [0 for _ in range(20)]
    tmp = list(map(str_int, input().split(' ')))
    for i in range(len(tmp)):
        string[tmp[i]] += 1
    ans = 0
    res = 0
    tmp = 0
    i = 9
    while(True):
        if (i<=0):
            break
        if(string[i] == 0):
            i -= 1
            tmp = 0
            continue
        if tmp != 0:
            tmp = tmp * string[i] + string[i]*string[i+1]*string[i+2]*string[i+3]*string[i+4]
            res += tmp
        else:
            tmp = string[i] * string[i+1] * string[i+2] * string[i+3] * string[i+4]
            res += tmp
        i-=1
    print ("{}\n".format(res))