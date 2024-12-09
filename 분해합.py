N = int(input())
answer = 0

for M in range(max(1, N - 9 * len(str(N))), N):
    sum_digits = sum(int(digit) for digit in str(M))  # M의 자리수 합
    if M + sum_digits == N:  # 분해합 계산
        answer = M  # 가장 작은 생성자 발견
        break

print(answer)
