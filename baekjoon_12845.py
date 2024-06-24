n = int(input())
cards = []
result = 0
cards=list(map(int, input().split()))
cards = sorted(cards,reverse = True)
first_card = cards[0]
for i in range(1,n):
    result += first_card + cards[i]
print(result)