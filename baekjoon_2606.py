from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n + 1)


def bfs(graph, s, visited):
    count = 1
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    retun
    count


result = bfs(graph, 1, visited)
print(result - 1)