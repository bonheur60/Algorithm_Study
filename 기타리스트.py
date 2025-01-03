n, s, m = map(int, input().split())
ans = {s}
vol = list(map(int, input().split()))

for v in vol:
    temp = set()

    for i in ans:
        if i + v <= m:
            temp.add(i + v)
        if i - v >= 0:
            temp.add(i - v)
    ans = temp
if not ans:
    print(-1)
else:
    print(max(ans))