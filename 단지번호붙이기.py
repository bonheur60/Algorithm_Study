import sys
from collections import deque

N = int(input())

# 각 집으로의 이동을 표현할 좌표리스트
# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 한 칸씩 이동할 좌표 설정 (x, y) => 동(1, 0), 서(-1, 0), 남(0, 1), 북(0, -1)
# 행렬 좌표 체계에서 행 : 위 -> 아래 증가, 열 : 왼 -> 오 증가
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(a, b):
    # count = 집의 개수
    count = 0

    q = deque()
    q.append((a, b))

    # 처음 방문한 곳에 대해 방문 처리
    graph[a][b] = 0

    while q:
        x, y = q.popleft()
        count += 1  # 결국엔 q에 들어가는 수와 각 단지의 집의 개수는 같기 때문에 여기서 count += 1 을 해줌

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
    return count


# 전체 단지의 수
total = 0
# 개별 단지의 집 갯수를 담아줄 리스트
nums_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            nums_list.append(bfs(i, j))
            total += 1  # bfs를 1회 진행하고 나면 한 단지 내의 모든 집에 대한 방문이 끝남
print(total)
for x in sorted(nums_list):
    print(x)