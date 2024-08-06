from collections import Counter
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
n_num = Counter(n_list)
answer = []
for i in m_list:
    if n_num[i] != 0 :
        answer.append(1)
    else:
        answer.append(0)
print(*answer)