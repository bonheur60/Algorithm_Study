from collections import deque

n, m, k = map(int, input().split())
trash = [list(map(int, input().split())) for _ in range(k)]

graph = [[0] * (m + 1) for _ in range(n + 1)]
for x, y in trash:
    graph[x][y] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0


def bfs(a, b):
    queue = deque([(a, b)])
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n + 1 and 0 <= ny < m + 1 and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


max_size = 0
for i in range(n + 1):
    for j in range(m + 1):
        if graph[i][j] == 1:
            max_size = max(max_size, bfs(i, j))
print(max_size)