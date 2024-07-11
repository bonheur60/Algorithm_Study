'''#1'''
from itertools import permutations
n,m = map(int,input().split())
array = list(map(int,input().split()))
array = sorted(array)

output = []
for num in list(permutations(array,m)):
    output.append(num)
output = sorted(list(set(output)))

for num in output:
    for n in num:
        print(n,end=' ')
    print()


'''#2'''
n,m = map(int,input().split())
nums = list(map(int, input().split()))
visited = [False] * n # 방문 여부
answers = []

def permuatation(nums,n,m,arr):
    if len(arr) == m:
        answers.append(arr[:]) # 정답 리스트에 추가
        return

    for i in range(len(nums)):
        if not visited[i]: # 방문하지 않은 경우만
            visited[i] = True # 방문 처리
            arr.append(nums[i])
            permuatation(nums,n,m,arr)
            visited[i] = False # 방문 해제
            arr.pop()

permuatation(nums,n,m,[])
answers = sorted(list(set(map(tuple, answers)))) # 중복 제거 및 정렬
for answer in answers:
    print(*answer,sep=' ')