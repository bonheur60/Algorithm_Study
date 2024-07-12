'''#1'''
from itertools import permutations,product
n,m = map(int,input().split())
num = list(i for i in range(1,n+1))

perm = product(num,repeat=m)
result = []
for p in perm:
    result.append(p)
for i in result:
    for j in i :
        print(j, end = ' ')
    print()


'''#2'''
n, m = map(int, input().split())

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()