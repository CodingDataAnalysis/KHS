from sys import stdin
from collections import deque
input = stdin.readline
N, K = map(int, input().rstrip().split())

peoples = deque([x for x in range(1, N+1)])
dummy = []

while peoples:
    for k in range(K-1):
        peoples.append(peoples.popleft())
    dummy.append(peoples.popleft())

print('<', end='')
print(*dummy, sep=', ', end='')
print('>')
