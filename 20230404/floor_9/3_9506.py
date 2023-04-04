# 약수들의 합

while True:
    n = int(input())
    if n < 1:
        break
    factor_list = []
    for i in range(1, n):
        if n % i == 0:
            factor_list.append(i)
    if sum(factor_list) == n:
        print(f'{n} = ', end='')
        print(*factor_list, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')