from collections import deque
MAX = 100001
n,k = map(int,input().split())
time = [-1]*MAX
def bfs(v):
    q = deque([v])
    time[v] = 0  # 시작 위치의 시간을 0으로 설정

    while q:
        location = q.popleft()
        if location == k:
            return time[location]

        for n_location in (location - 1, location + 1, 2 * location):
            if 0 <= n_location < MAX and time[n_location] == -1:
                if n_location == 2 * location:
                    time[n_location] = time[location]
                    q.appendleft(n_location)
                else:
                    time[n_location] = time[location] + 1
                    q.append(n_location)
print(bfs(n))            