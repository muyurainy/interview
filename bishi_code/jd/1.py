n = int(input())
tree = {}
for _ in range(n-1):
    i, j = map(int, input().split(' '))
    if i in tree:
        tree[i].append(j)
    else:
        tree[i] = [j]
    if j in tree:
        tree[j].append(i)
    else:
        tree[j] = [i]
print (tree)