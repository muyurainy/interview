n = int(input())
nums = list(map(int, input().split(' ')))
K = int(input())
nums = sorted(nums)
count = 0
if len(nums) <= 2 or n <= 0:
    print(0)
else:
    for i in range(len(nums) - 2):
        k, j = i+1, len(nums) - 1
        while (k < j):
            if nums[k] + nums[j]  < K - nums[i]:
                count += (j - k)
                # print (nums[i], nums[k], nums[j])
                k += 1
            else:
                j -= 1
    print(count)
