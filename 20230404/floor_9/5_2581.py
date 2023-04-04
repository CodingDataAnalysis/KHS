# 소수

M = int(input())
N = int(input())

factor_list = []
for i in range(M, N+1):
    factor_count = 0
    for j in range(1, i):
        if i % j == 0:
            factor_count += 1
    if factor_count == 1:
        factor_list.append(i)
if factor_list:
    print(sum(factor_list), factor_list[0], sep='\n')
else:
    print('-1')

