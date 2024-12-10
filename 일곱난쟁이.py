from itertools import combinations
Dwarf = []
for _ in range(9):
    Dwarf.append(int(input()))
Dwarf_people = combinations(Dwarf,7)
for i in Dwarf_people:
    each_Dwarf = list(i)
    if sum(each_Dwarf) == 100:
        result = sorted(each_Dwarf)
for i in result:
    print(i)