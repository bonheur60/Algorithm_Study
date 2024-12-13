n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(map(str, input().rstrip())))
cnt = []
for a in range(n - 7):  # 8*8로 자르기 위해, -7해준다
    for b in range(m - 7):
        w_index = 0  # 흰색으로 시작
        b_index = 0  # 검은색으로 시작

        for i in range(a, a + 8):  # 시작지점
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:  # 짝수인 경우
                    if chess[i][j] != 'W':  # 짝수면 처음 색과 동일해야함
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if chess[i][j] != 'W':  # 홀수면 처음 색과 달라도됨
                        b_index += 1
                    else:
                        w_index += 1

        cnt.append(w_index)  # W로 시작할 때 경우의 수
        cnt.append(b_index)  # B로 시작할 때 경우의 수
print(min(cnt))