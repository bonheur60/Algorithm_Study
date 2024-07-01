n = int(input())
road = list(map(str, input().strip()))
d = [1000001] * len(road)
d[0] = 0
for i in range(1, len(road)):
    # 글자가 B일때
    if road[i] == 'B':
        for j in range(0, i):
            if road[j] == 'J':
                d[i] = min(d[i], (i - j) * (i - j) + d[j])
    # 글자가 O일떄
    elif road[i] == 'O':
        for j in range(0, i):
            if road[j] == 'B':
                d[i] = min(d[i], (i - j) * (i - j) + d[j])

    # 글자가 J일때
    else:
        for j in range(0, i):
            if road[j] == 'O':
                d[i] = min(d[i], (i - j) * (i - j) + d[j])

if d[n - 1] == 1000001:
    print(-1)
else:
    print(d[n - 1])