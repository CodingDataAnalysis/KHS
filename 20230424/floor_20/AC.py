from sys import stdin
from collections import deque

input = stdin.readline
T = int(input())

for t in range(T):
    s = input().rstrip()
    n = int(input())
    flag = 0 
    
    arr = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        arr = []

    for char in s:
        if char == 'R':
            flag += 1
        elif char == 'D':
            if len(arr) == 0:
                print('error')
                break
            else:
                if flag % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    else:
        if flag % 2 == 0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')
    
