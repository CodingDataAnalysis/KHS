# 소수 찾기 

N = int(input())
num_list = map(int, input().split())
isFactorNum = 0

for num in num_list:
    factor_count = 0
    for i in range(1, num):
        if num % i == 0:
            factor_count += 1
    if factor_count == 1:
        isFactorNum += 1
print(isFactorNum)