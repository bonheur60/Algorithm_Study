from collections import Counter
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
n_num = Counter(n_list)
for j in m_list:
    if n_num[j] != 0 :
        print(1)
    else:
        print(0)