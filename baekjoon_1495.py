n,s,m = map(int,input().split())
#곡 순서에서 변경할 수 있는 볼륨 차
v = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        #현재 i곡의 볼륨이 담겨있으면
        if dp[i][j] == 1:
            min_val = j - v[i]
            max_val = j + v[i]
            # 줄인 볼륨이 0보다 크거나 같을 경우 다음곡에 현재 볼륨 담기
            if min_val >= 0 :
                dp[i+1][min_val] = 1
            # 키운 볼륨이 m 보다 작을 경우 다음 곡에 현재 볼륨 담기
            if max_val <= m:
                dp[i+1][max_val] = 1
result = -1
#볼륨의 최대값을 출력하기 위해 내림차순으로 반복문 실행
for i in range(m,-1,-1):
    if dp[n][i] == 1:
        result = i
        break
print(result)