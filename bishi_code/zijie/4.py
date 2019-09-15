n, X = map(int, input().split(' '))
a, b, w = [], [], []
for _ in range(n):
    tmp_a, tmp_b, tmp_w = map(int, input().split(' '))
    a.append(tmp_a)
    b.append(tmp_b)
    w.append(tmp_w)
print(a, b ,w)
mask = [False] * (n + 1)
max_count = [0]
# cur_a 优惠金额 cur_b 总预算 cur_w 快乐值
def solve(index, a, b, w, max_count, X, cur_a, cur_b, cur_w):
    if index == len(a):
        max_count[0] = max(cur_w, max_count[0])
        return
    for i in range(index, len(a)):  
        if cur_a + a[i] - b[i] >= cur_b + b[i] - X:
            solve(i + 1, a, b, w, max_count, X, cur_a + a[i] - b[i], cur_b + b[i], cur_w+w[i])
        solve(i+1, a, b, w, max_count, X, cur_a, cur_b, cur_w)


for i in range(n):
    solve(i, a, b, w, max_count, X, 0, 0, 0)
print(max_count[0])