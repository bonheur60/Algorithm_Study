from collections import deque

m, n = map(int, input().split())  # 가로 세로
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
queue = deque([])

# 익은 토마토의 위치 queue에 추가
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])


# BFS 함수 정의
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                # 상하좌우에 익지 않은 토마토(0)이 있으면 1을 더해 몇번쨰인지 세주기
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])


# BFS: 토마토 익히기 시작
bfs()

# BFS 종료 .
for i in matrix:
    for j in i:
        if j == 0: 후  # 익지 않은 토마토가 있으면(=토마토가 모두 익지 못하는 상황) -1 출력
        print(-1)
        exit()  # 다음 행의 여부와 관계 없이 -1만 출력해야하므로 종료시킴
else:
    cnt = max(cnt, max(i))  # 그래프에서 가장 큰 값이 마지막으로 익은 토마토임 → 한 줄씩 최댓값을 day로 갱신하며 최댓값 찾기
print(cnt - 1)
# 처음 시작을 0이 아닌 1부터 했으므로 -1을 해야 날짜를 구할 수 있음     