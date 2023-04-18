# 어떤 수 N의 약수 개수와, 수에 대한 약수 전체가 주어졌을 때,
# N을 구하는 프로그램을 작성하시오

from sys import stdin
factor_num = int(stdin.readline())
factor = list(map(int, stdin.readline().rstrip().split()))

print(max(factor) * min(factor))

