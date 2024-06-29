number = list(map(int, input().rstrip()))
answer = ""
if 0 not in number :
    print(-1)
elif sum(number) % 3 != 0 :
    print(-1)
else:
    number = sorted(number,reverse=True)
    for n in number:
        answer += str(n)
print(answer)