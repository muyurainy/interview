def solution():
    '''题目大意：Manao要依次经过一些怪物，每个怪物具有两个属性战斗力和贿赂所需的金钱，
    一开始Manao没有战斗力，他通过贿赂怪兽使其成为自己的战斗力，要是Manao当前经过的怪
    兽的战斗力比Manao的战斗力高，怪兽就会攻击他，Manao就必须贿赂怪兽，反之，Manao可
    以选择贿赂或直接过去，求经过一系列怪兽所花费的最少的金钱数。此题经分析为动态规划，
    要求的最优解为最少钱数，而状态为（i，j），表示当前经过第i个怪兽时战斗力为j，
    money(i,j)->money(i+1,j+dread[i])+price[i]或money(i+1,j)，答案是money(n,j)中最小值。
    输入:（第二行武力值，第三行收买价值）
    3
    8 5 9
    1 1 2

    Notes
    -----
    动态规划
    '''
    n = int(input())
    dread = []
    price = []
    dread = list(map(int, input().split()))
    price = list(map(int, input().split()))
    mon = [{} for i in range(n)]
    mon[0][dread[0]] = price[0]
    for i in range(1, n):
        k = 4e9
        for j in mon[i-1]:
            if j < dread[i]:
                t = mon[i][j + dread[i]] = mon[i-1][j] + price[i]
                if k>t:
                    k = t
            else:
                t = mon[i][j] = mon[i-1][j]
                mon[i][j + dread[i]] = mon[i-1][j] + price[i]
                if k>t:
                    k = t
    print (k)

solution()