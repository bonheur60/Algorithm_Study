from collections import deque
def bfs(v):
    q = deque([v])
    while q:
        location = q.popleft()
        if location == k :
            return array[location]
        for next_location in (location-1,location+1,2*location):
            if 0<=next_location < MAX and not array[next_location]:
                array[next_location] = array[location] + 1
                q.append(next_location)

n,k = map(int,input().split())
MAX = 1000001
array = [0] * MAX
print(bfs(n))