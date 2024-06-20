# BFS
import sys
sys.setrecursionlimit(10000)
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

# 입력을 받는 부분
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보를 받는 부분
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 방문 기록 및 연결 요소 카운트 초기화
visited = [False] * (n + 1)
count = 0

# 모든 노드를 검사하여 연결 요소를 찾는 부분
for i in range(1, n + 1):
    if visited[i] == False:
        bfs(graph, i, visited)
        count += 1

# 결과 출력
print(count)

#DFS
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if visited[i] == False:
        count += 1
        dfs(graph, i, visited)
print(count)