from collections import deque

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순서대로 방문하기 위해 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS 함수
def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

# BFS 함수
def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# DFS 실행
visited = [False] * (n + 1)
dfs(v)
print()  # 줄바꿈

# BFS 실행
visited = [False] * (n + 1)
bfs(v)
