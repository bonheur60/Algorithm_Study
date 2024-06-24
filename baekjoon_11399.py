n = int(input())
times = list(map(int,input().split()))
times = sorted(times)
time = 0
for i in range(n):
    for j in range(0,i+1):
        time += times[j]
print(time)