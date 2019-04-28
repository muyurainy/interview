n, w = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
a = sorted(a)
girl_min = a[0]
boy_min = a[n]
if girl_min < (boy_min / 2):
    all_min = girl_min
else:
    all_min = boy_min / 2
#all_min = girl_min if girl_min >= boy_min / 2 else boy_min / 2
if all_min * 3 * n > w:
    print ('%.6f' % (1.0 * w))
else:
    print ('%.6f' % (3 * n * all_min))
