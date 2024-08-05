from collections import Counter
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
n_count = Counter(n_list)
for i in m_list:
    print(n_count[i],end = ' ')