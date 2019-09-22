n = int(input())
nums = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    nums.append((a, b))
nums = sorted(nums, key = lambda x: x[0])
#print(nums)
maxC = nums[0][1]
curC = nums[0][1]
t = nums[0][0]
for i in range(1, n):
    curC -= (nums[i][0] - t)
    curC = curC if curC >= 0 else 0
    curC += nums[i][1]
    maxC = curC if maxC < curC else maxC
    t = nums[i][0]
t += curC
print ('{} {}'.format(t, maxC))
