# -*- coding: utf-8 -*-

def edit_Distance(word1, word2):
    '''给定两个字符串，由一个转成另一个所需的最少编辑操作次数

    Parameter
    ---------
    word1, word2
    Return
    ------
    最小编辑距离dp[i][j]
    '''
    dp = [[i+j for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    for i in range(1, len(word1) + 1):
        dp[i][0] = i
    for j in range(1, len(word2) + 1):
        dp[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            flag = 0 if word1[i-1] == word2[j-1] else 1 
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + flag)
    return dp[len(word1)][len(word2)]

def edit_Distance_R(word1, word2):
    '''给定两个字符串，由一个转成另一个所需的最少编辑操作次数

    Parameter
    ---------
    word1, word2
    Return
    ------
    最小编辑距离dp[i][j]
    Notes
    -----
    递归版本
    '''
    def _edit_distance(word1, word2, i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        flag = 0 if word1[i-1] == word2[j-1] else 1 
        return min(_edit_distance(word1, word2, i-1, j) + 1, _edit_distance(word1, word2, i, j - 1) + 1, _edit_distance(word1, word2, i-1, j-1) + flag)
    return _edit_distance(word1, word2, len(word1), len(word2))
    
'''
word1 = input()
word2 = input()
print (edit_Distance_R(word1, word2))
'''