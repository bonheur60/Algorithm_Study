from itertools import combinations
n,s = map(int,input().split())
array = list(map(int, input().split()))
cnt = 0
for i in range(1,n+1):
    arr_com = combinations(array,i)
    for a in arr_com :
        if sum(a) == s:
            cnt +=1
print(cnt)