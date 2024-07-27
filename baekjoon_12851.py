from collections import deque
n,k = map(int,input().split())

def bfs(v):
    global cnt
    q = deque([v])
    while q:
        location = q.popleft()
        if location == k :
            cnt +=1
            continue
        for next_location in (location-1,location+1, 2*location):
            if 0<= next_location < MAX and (array[next_location] == 0 or array[next_location] == array[location]+1):
                array[next_location] = array[location]+1
                q.append(next_location)

MAX = 1000001
cnt = 0
array = [0]*MAX
bfs(n)


print(array[k])
print(cnt)