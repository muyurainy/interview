# coding: utf-8
'''
kuaishou interview
'''

'''快手一面
'''


def sort():
    pass


'''快手二面 有2N个数的int数组，两两组成一个pair，求pair和的最大值和最小值差值的最小值
'''


def kuaishou_2():
    data = [1, 2, 4, 4]
    data = sorted(data)
    N = len(data)
    pair_data = [data[i] + data[N-1-i] for i in range(N // 2)]
    print(pair_data)
    min_pair, max_pair = min(pair_data), max(pair_data)
    print(max_pair-min_pair)


if __name__ == '__main__':
    kuaishou_2()
