K,N = map(int,input().split())
cables = []
for _ in range(K):
    cables.append(int(input()))
start = 1
end = max(cables)
while start <= end :
    mid = (start+end)//2
    len_num = 0
    for cable in cables:
        len_num += cable // mid
    if len_num >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)