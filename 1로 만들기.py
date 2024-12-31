# 1. 문제의 input을 받기
N = int(input())

# 2. 최솟값 계산을 위해 초기 값을 최대 값으로 세팅하기
INF = int(10e9)
DP = [INF for _ in range(1000001)]

# 3. DP의 작은 문제 답 구하기
DP[1] = 0
DP[2] = 1
DP[3] = 1

# 4. 설정한 관계식에 맞게 DP 탐색 진행하기
for i in range(4,N+1):
    min_way = INF
    if i % 3 == 0:
        min_way = min(min_way, DP[i//3])
    if i%2 == 0:
        min_way = min(min_way , DP[i//2])
    min_way = min(min_way, DP[i-1])
    DP[i] = min_way + 1

print(DP[N])