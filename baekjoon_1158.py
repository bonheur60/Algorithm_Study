from collections import deque
import sys

N,K = map(int,input().split())

d = deque()
answer = []

for i in range(1, N + 1):
    d.append(i)

while len(d) > 0:
    for j in range(1, K):
        d.append(d.popleft())
    answer.append(str(d.popleft()))

print("<{}>".format(', '.join(answer)))