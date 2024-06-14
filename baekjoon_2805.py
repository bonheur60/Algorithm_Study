n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    rest = 0

    for tree in trees:
        if tree > mid:
            rest += tree - mid

    if rest >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)