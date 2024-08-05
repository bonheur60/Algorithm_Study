n = int(input())
arr = list(map(int,input().split()))
sorted_arr = sorted(set(arr))
compression = {k:v for v,k in enumerate(sorted_arr)}
result = [compression[x] for x in arr]
for i in result:
    print(i, end = ' ')