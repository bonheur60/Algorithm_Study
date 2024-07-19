from itertools import combinations

for _ in range(4):

    tmp_result = list(map(int, input().split()))
    game_result = [tmp_result[i:i + 3] for i in range(0, 16, 3)]

    answers = []
    game = list(combinations(range(6), 2))


    def dfs(round):
        if round == 15:
            cnt = 1

            for g in game_result:  # 각 나라의 결과를 확인
                if g.count(0) != 3:  # 승, 무, 패 각각이 0이 아닌 경우가 있으면 불가능한 경우
                    cnt = 0
                    break

            answers.append(cnt)
            return

            # 전체 경기 15번의 조합
        t1, t2 = game[round]

        # 각 경기의 승부패
        for x, y in ((0, 2), (1, 1), (2, 0)):
            if game_result[t1][x] > 0 and game_result[t2][y] > 0:
                game_result[t1][x] -= 1
                game_result[t2][y] -= 1

                dfs(round + 1)

                game_result[t1][x] += 1
                game_result[t2][y] += 1


    dfs(0)
    if 1 in answers:
        print(1)
    else:
        print(0)