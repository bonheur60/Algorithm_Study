Money = int(input())
MachineDuck = list(map(int, input().split()))

# 준현
n_jusic=0
j_money = Money
for j in MachineDuck:
    if j_money >= j:
        n_jusic += j_money//j
        j_money = j_money%j

# 성민
s_jusic = 0
s_money = Money
for i in range(3,len(MachineDuck)):
    if (MachineDuck[i-3]>MachineDuck[i-2]) and (MachineDuck[i-2]>MachineDuck[i-1]) and (MachineDuck[i-1]>MachineDuck[i]):
        if s_money >= MachineDuck[i]:
            s_jusic += s_money//MachineDuck[i]
            s_money = s_money%MachineDuck[i]

j_sum = j_money+n_jusic*MachineDuck[-1]
s_sum = s_money+s_jusic*MachineDuck[-1]
if j_sum > s_sum:
    print("BNP")
elif j_sum < s_sum:
    print("TIMING")
else:
    print("SAMESAME")