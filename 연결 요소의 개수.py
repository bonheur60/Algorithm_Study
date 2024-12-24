from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n + 1)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


count = 0
for i in range(1, n + 1):
    if visited[i] == False:
        bfs
        count += 1
print(count)
