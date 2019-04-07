n,k = map(int, input().split(' '))
num = 0
for _ in range(k):
    if n == 1:
        break
    n = int(n/2)
    k -= 1
    num += 1
print (num + k)