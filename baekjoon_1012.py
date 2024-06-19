#DFS
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0  # 배추흰지렁이 마리 수
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1  # dfs 탐색이 끝날때 result += 1
    print(result)
#BFS
import sys
from collections import deque

sys.setrecursionlimit(10000)


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0
    return


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)