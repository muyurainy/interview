n, X = map(int, input().split(' '))
visited = [0] * 500
max_count = [0]
def DFS(k, sail, cost, w, max_count):
    if cost > X and sail < cost - X:
        return
    if visited[k]:
        return
    visited[k] = 1
    sail += game[k][3]
    max_count[0] = max(max_count[0], w)
    for i in range(k+1, n):
        if not visited[i]:
            DFS(i, sail + game[i][3], cost + game[i][1], w+game[i][2], max_count)

game = []
for _ in range(n):
    tmp_a, tmp_b, tmp_w = map(int, input().split(' '))
    game.append((tmp_a, tmp_b, tmp_w, tmp_a - tmp_b))
game = sorted(game, key=lambda x: x[1])
for i in range(n):
    DFS(i, game[i][3], game[i][1], game[i][2], max_count)
print (max_count[0])