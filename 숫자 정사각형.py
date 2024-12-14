n,m = map(int,input().split())
num_arr = []
for _ in range(n):
    num_arr.append(list(input()))
check = min(n,m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i+k)<n) and ((j+k)<m) and (num_arr[i][j] == num_arr[i][j+k]==num_arr[i+k][j]==num_arr[i+k][j+k]):
                answer = max(answer, (k+1)**2)
print(answer)