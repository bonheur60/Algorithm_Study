n = int(input())
times = []
for _ in range(n):
    s,e = map(int,input().split())
    times.append((s,e))
times.sort(key=lambda x : (x[1],x[0]))
fe_time = times[0][0]
count = 0
for i in range(n):
    if times[i][0] >= fe_time:
        count +=1
        fe_time = times[i][1]
print(count)