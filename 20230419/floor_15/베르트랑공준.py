# n < f <= m 을 만족하는 소수 f가 최소 하나 있다.
# f의 개수를 구하세요.
# while 을 언제까지고 반복하므로
# 범위 내에서 에라토스테네스의 체로 미리 소수범위를 구함
from math import sqrt

eratosthenes = [False, False] + [True]*246911
for i in range(2, int(sqrt(len(eratosthenes)))+1):
    if eratosthenes[i]:
        for j in range(i*2, len(eratosthenes)+1, i):
            eratosthenes[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    m = 2 * n
    count = 0
    for i in range(n+1, m+1):
        if eratosthenes[i]:
            count +=1
    print(count)