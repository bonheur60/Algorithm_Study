"""#1"""
from itertools import combinations

test_cases = []
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    test_cases.append(n[1:])

for idx, case in enumerate(test_cases):
    # 중복 제거 및 오름차순 정렬
    m = sorted(list(set(case)))

    # 6개의 원소로 이루어진 조합 생성
    answer = list(combinations(m, 6))

    # 조합 출력
    for comb in answer:
        print(" ".join(map(str, comb)))

    # 마지막 테스트 케이스가 아닌 경우 빈 줄 출력
    if idx < len(test_cases) - 1:
        print()
        
"""#2"""
while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break

    nums.pop(0)
    V = 6
    stack = []


    def dfs():
        if len(stack) == V:
            print(*stack)
            return

        if len(stack) == 0:
            for i in nums:
                stack.append(i)
                dfs()
                stack.pop()
            return

        for i in nums:
            if i > stack[-1]:
                stack.append(i)
                dfs()
                stack.pop()


    dfs()
    print()