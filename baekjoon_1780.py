N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 종이의 개수
cnt = []


# 분할 정복
def divide(x, y, n):
    color = matrix[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):

            # 색깔이 다르면 분할 정복
            if color != matrix[i][j]:
                for a in range(3):
                    for b in range(3):
                        divide(x + (n // 3) * a, y + (n // 3) * b, n // 3)
                return

    if color == 1:
        cnt.append(1)
    elif color == -1:
        cnt.append(-1)
    else:
        cnt.append(0)


divide(0, 0, N)
print(cnt.count(-1), cnt.count(0), cnt.count(1), sep='\n')