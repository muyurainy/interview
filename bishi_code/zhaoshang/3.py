n = int(input())
a = list(map(int, input().split(' ')))
num = 0
for i in range(len(a)):
    if a[i] % 2 == 1:
        a[i] -= 1
        if num == 0:
            num += 1

def isEnd(a):
    flag = a[0]
    for i in range(1, len(a)):
        if a[i] != flag:
            return False
    return True

def pro_max(a, num1):
    num = 0
    for i in range(len(a)):
        if a[i] == num1:
            a[i] = a[i] // 2
            num += 1
    return num

def pro_min(a, num1):
    num = 0
    for i in range(len(a)):
        if a[i] == num1:
            a[i] *= 2
            num += 1
    return num


while (not isEnd(a)):
    _min = min(a)
    _max = max(a)
    _min_count = a.count(_min)
    _max_count = a.count(_max)
    if _min_count < _max_count:
        num += pro_min(a, _min)
    else:
        num += pro_max(a, _max)
    #print (a)
print (num)
    