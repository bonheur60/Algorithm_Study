from collections import deque

game = [list(input().rstrip()) for _ in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0


def bfs(x, y):
    queue = deque([(x, y)])
    now = game[x][y]
    pos = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < 12 and 0 <= ny < 6 and game[nx][ny] == now and not visited[nx][ny]:
                pos.append((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = 1

    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for i, j in pos:
            game[i][j] = '_'
            bomblist.append((i, j))


while True:
    visited = [[0] * 6 for _ in range(12)]
    bomblist = []

    for i in range(12):
        for j in range(6):
            if game[i][j] != '.' and game[i][j] != '_' and not visited[i][j]:
                bfs(i, j)

    if len(bomblist) == 0:
        break

    for bomb in bomblist:
        x, y = bomb[0], bomb[1]
        for i in range(x, 0, -1):
            game[i][y] = game[i - 1][y]
        game[0][y] = '.'

    time += 1

print(time)