from collections import deque
from sys import stdin
input = stdin.readline
queue = deque()

N = int(input())
for n in range(N):
    order = input().rstrip()
    if 'push' in order:
        queue.append(int(order.split()[1]))
    elif order == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif order == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)