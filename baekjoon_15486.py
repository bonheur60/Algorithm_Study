n = int(input())
c = []
for _ in range(n):
    c.append(list(map(int,input().split())))
m = len(c[0])
now = 0
dp = [0] * (n + 1)

#c[i][0]은 시간 and c[i][1]은 돈

for i in range(n):
    now = max(now, dp[i])
    if i + c[i][0] > n:
        continue
    # 현재까지의 수익에 이번주 상담의 수익을 더한 값과 오늘의 상담이 끝나는 시점의 수익 중 큰 값
    dp[i + c[i][0]] = max(now + c[i][1], dp[i + c[i][0]])

print(max(dp))