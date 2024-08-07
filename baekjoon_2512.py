n = int(input())
n_list = list(map(int,input().split()))
n_target = max(n_list)
country_sum = int(input())
result = 0
start = 0
end = max(n_list)
while start <= end :
    mid = (start+end)//2
    total = 0
    for i in n_list:
        if i > mid :
            total += mid
        else:
            total += i
    if total <= country_sum:
        result = mid
        start = mid +1
    else:
        end = mid -1
print(result)