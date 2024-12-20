n = int(input())
team_power = []
for _ in range(n):
    team_power.append(list(map(int, input().split())))

# 팀나누기
from itertools import combinations


def generate_teams(n):
    teams = [i for i in range(1, n + 1)]
    m = n // 2
    all_combinations = list(combinations(teams, m))
    each_team = []

    for team1 in all_combinations:
        team2 = tuple(set(teams) - set(team1))
        if team1 < team2:  # 중복을 방지하기 위해 team1이 team2보다 작은 경우만 선택
            each_team.append((team1, team2))

    return each_team


team_num = generate_teams(n)

# 최솟값 초기화
min_diff = float('inf')

# 점수 계산 및 최솟값 찾기
for i in range(len(team_num)):
    team_number = list(team_num[i])

    # Start 팀 점수 계산
    start_team = 0
    for a, b in combinations(team_number[0], 2):  # team_number[0]에서 2명씩 조합
        start_team += team_power[a - 1][b - 1] + team_power[b - 1][a - 1]

    # Link 팀 점수 계산
    link_team = 0
    for c, d in combinations(team_number[1], 2):  # team_number[1]에서 2명씩 조합
        link_team += team_power[c - 1][d - 1] + team_power[d - 1][c - 1]

    # 점수 차이 계산 및 최솟값 갱신
    diff = abs(start_team - link_team)
    min_diff = min(min_diff, diff)

# 결과 출력
print(min_diff)