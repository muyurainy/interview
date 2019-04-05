def solution():
    '''题目大意：Manao要依次经过一些怪物，每个怪物具有两个属性战斗力和贿赂所需的金钱，
    一开始Manao没有战斗力，他通过贿赂怪兽使其成为自己的战斗力，要是Manao当前经过的怪
    兽的战斗力比Manao的战斗力高，怪兽就会攻击他，Manao就必须贿赂怪兽，反之，Manao可
    以选择贿赂或直接过去，求经过一系列怪兽所花费的最少的金钱数。此题经分析为动态规划，
    要求的最优解为最少钱数，而状态为（i，j），表示当前经过第i个怪兽时战斗力为j，
    money(i,j)->money(i+1,j+dread[i])+price[i]或money(i+1,j)，答案是money(n,j)中最小值。
    输入:
    4
    1100

    Notes
    -----
    直接从左到右循环去判断
    '''
    _, string = int(input()), input()
    old_length = 0
    new_str = ""
    while old_length != len(string) and len(string) >= 2:
        index = 0
        while index < len(string):
            if index == len(string) - 1:
                new_str += string[index]
                break
            if string[index] == string[index+1]:
                new_str += string[index]
                index += 1
            else:
                index += 2
        old_length = len(string)
        string = new_str
        new_str = ""
    print (len(string))

solution()