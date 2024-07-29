n,k = map(int,input().split())
bag = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(k+1)
for item in bag:
    w,v = item
    for i in range(k,w-1,-1):
        dp[i] =max(dp[i],dp[i-w]+v)
print(dp[-1]) #최댓값 출력 