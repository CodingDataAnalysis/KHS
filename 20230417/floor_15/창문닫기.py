# 약수가 홀수면 루프가 끝날 때 열린 창으로 끝남
# 약수가 홀수인 수는 sqrt(4) == 2 처럼
# 제곱근을 씌웠을 때 정수로 떨어지는 수 
# == 제곱수 
from sys import stdin
from math import sqrt
windows = int(stdin.readline())

start = 1
count = 0
while start <= windows:
    if str(sqrt(start)).endswith('.0'):
        count += 1
    start += 1
print(count)