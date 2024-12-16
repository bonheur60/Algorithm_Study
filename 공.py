n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
graph = [1,2,3]
for a,b in arr:
    for i,j in enumerate(graph):
        if j == a :
            graph[i]= b
        elif j == b :
            graph[i] = a
print(graph[0])