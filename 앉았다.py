import sys
input = sys.stdin.readline

a, b = map(int, input().split())
total = 9*17
ans = 0

if a == b:
    ans = total - (10-a)
else:
    mypoint = (a+b) % 10
    for i in range(1, 11):
        for j in range(i+1, 11):
            if mypoint > (i+j) % 10:
                if i == a and j == b:
                    continue
                elif i == a or j == a or i == b or j == b:
                    ans += 2
                else:
                    ans += 4

print("%.3f" % (ans / total))