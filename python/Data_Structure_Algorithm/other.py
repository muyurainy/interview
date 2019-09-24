# -*- coding: utf-8 -*-

'''
# 其它类型的题目
'''

'''
# 题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

def PrintMinNumber(numbers):
    def cmp_str(x, y):
        if x+y > y+x:
            return 1
        elif x+y == y+x:
            return 0
        else:
            return -1
    import functools
    num_str = [str(item) for item in numbers]
    return ''.join(sorted(num_str, key = functools.cmp_to_key(cmp_str)))

numbers = [3, 11, 123]
print(PrintMinNumber(numbers))

