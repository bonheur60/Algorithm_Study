from itertools import combinations_with_replacement

t = int(input())
test_case = []
for _ in range(t):
    test_case.append(int(input()))
max_num = max(test_case)
all_Ti = []
i = 1
while True:
    T_i = i * (i + 1) // 2
    if T_i > max_num:
        break
    all_Ti.append(T_i)
    i += 1

for k in test_case:
    flag = False

    for comb in combinations_with_replacement(all_Ti, 3):
        if sum(comb) == k:
            flag = True
            break
    print(1 if flag else 0)