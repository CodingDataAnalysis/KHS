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