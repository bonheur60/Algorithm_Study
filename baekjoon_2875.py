n, m, k = map(int, input().split())

max_teams = min(n // 2, m)

remaining_mem = (n - max_teams * 2) + (m - max_teams)

if remaining_mem >= k:
    print(max_teams)
else:
    additional_mem_need = k - remaining_mem

    teams_to_disband = (additional_mem_need + 2) // 3

    print(max_teams - teams_to_disband)