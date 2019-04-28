n = int(input())
a = 2
res = 1
if (n >= 6):
    c = 666666666
    N = n - 6
    while N!=0:
        if (N % 2 == 1):
            res = (res * a) % c
        a = (a * a) % c
        N = N // 2
    print (res)
else:
    print(0)