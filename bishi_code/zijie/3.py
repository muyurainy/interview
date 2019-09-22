n = int(input())
nums = list(map(int, input().split(' ')))
nums.insert(0, 0)
sums = [0] * (n+1)
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    sums[i] = sums[i-1] + nums[i]
    dp[i][i] = nums[i]
for i in range(n, 0, -1):
    for j in range(i + 1, n+1):
        dp[i][j] = sums[j] - sums[i - 1] - min(dp[i+1][j], dp[i][j-1])

print(dp[1][n])
