from sys import stdin
input = stdin.readline
n = int(input())

num = 1
stack = []
result = []

for _ in range(n):
    target = int(input())
    while target >= num:
        stack.append(num)
        result.append('+')
        num += 1
    if stack.pop() == target:
        result.append('-')
    else:
        print('NO')
        exit()

print('\n'.join(result))