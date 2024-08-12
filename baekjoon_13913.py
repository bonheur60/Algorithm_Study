from collections import deque
MAX = 100001
#수빈이가 특정 위치를 방문 할때 걸리는 시간을 나타내는 값
visited = [0]*MAX
#자식 노드가 부모 노드를 알기 위한 정보
check = [0]*MAX
n,k = map(int,input().split())
def move(location):
    data = []
    temp = location
    for _ in range(visited[location]+1):
        data.append(temp)
        temp = check[temp]
    print(' '.join(map(str,data[::-1])))
def bfs():
    q = deque()
    q.append(n)
    while q:
        location = q.popleft()
        if location == k :
            print(visited[location])
            move(location)
            return
        for n_location in (location-1,location+1, 2*location):
            if 0<= n_location < MAX and not visited[n_location]:
                visited[n_location]= visited[location]+1
                q.append(n_location)
                check[n_location] = location
bfs()
