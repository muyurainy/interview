def find_min(a):
    min_num = max(a) + 1
    for i in a:
        if min_num > i and i != 0:
            min_num = i
    if min_num == max(a) + 1:
        min_num = 0
    return min_num

n, k = map(int, input().split(' '))
a = list(set(map(int, input().split(' '))))
a = sorted(a)
index = 0
tmp = 0
for i in range(len(a)):
    if index >= k:
        break
    if a[i] > 0:
        print(a[i] - tmp)
        tmp += a[i]
        index += 1
    if min(a) == 0:
        print (0)
        break