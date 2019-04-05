def solution():
    '''你就要去购物了，现在你手上有N种不同面值的硬币，
    每种硬币有无限多个。为了方便购物，你希望带尽量少
    的硬币，但要能组合出1到X之间的任意值。
    输入:
    20 4
    1
    2
    5
    10

    Notes
    -----
    直接贪心去做, 需要注意这里的小技巧就是sum从0开始，
    而sum_m += mon[m-1-i]
    '''
    n, m = map(int, input().split(' '))
    sum_m = 0
    num = 0
    mon = []
    for i in range(m):
        mon.append(int(input()))
    mon = sorted(mon)
    if mon[0] != 1:
        print (-1)
        return
    while(True):
        if sum_m >= n:
            print (num)
            break
        for i in range(m):
            if sum_m + 1 >= mon[m-1-i]:
                sum_m += mon[m-1-i]
                num += 1
                break
    return
solution()