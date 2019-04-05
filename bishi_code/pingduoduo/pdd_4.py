def oper(w1, w2):
    dp = [[i+j for j in range(len(w2) + 1)] for i in range(len(w1) + 1)]
    for i in range (1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            if w1[i-1] == w2[j-1]:
                flag = 0
            else:
                flag = 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + flag)
    return dp[-1][-1]

w1 = input()
w2 = input()
print (oper(w1, w2))