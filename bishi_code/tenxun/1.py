n, k = map(int, input().split(' '))
base = 1
index = 0
while(True):
    if base > k:
        break
    base = base * 2 + 1
    index += 1
if n % int(pow(2, index)) == 0:
    print (n // int(pow(2, index)) + index)
else:
    print ((n // int(pow(2, index))) + 1 + index)