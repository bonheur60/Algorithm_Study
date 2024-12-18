def check(tmp):
    # 가로
    for i in range(5):
        if bingo_board[i] == [0] * 5:
            tmp += 1

            # 세로
    for i in range(5):
        if all(bingo_board[j][i] == 0 for j in range(5)):
            tmp += 1

    # 대각선 1
    if all(bingo_board[i][i] == 0 for i in range(5)):
        tmp += 1

        # 대각선 2
    if all(bingo_board[i][4 - i] == 0 for i in range(5)):
        tmp += 1

    return tmp


bingo_board = []
for _ in range(5):
    bingo_board.append(list(map(int, input().split())))
speaking = []
for _ in range(5):
    speaking += list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if speaking[i] == bingo_board[x][y]:
                bingo_board[x][y] = 0
                cnt += 1
    if cnt >= 12:
        result = check(tmp)
        if result >= 3:
            print(i + 1)
            break 