n,k = map(int,input().split())
wallets = []
for _ in range(n):
    wallets.append(int(input()))
wallets = sorted(wallets,reverse = True)
cnt = 0
for coin in wallets:
    if k >= coin:
        cnt += k // coin
        k %= coin #나머지 금액을 다음으로 큰 동전부터 계속해서 계산
        if k <= 0:
            break
print(cnt)