from sys import stdin
input = stdin.readline
n = int(input())

for i in range(n):
    s = input().rstrip()
    for j in range(len(s)//2+1):
        s = s.replace('()', '')
    if len(s) == 0 or s.isspace():
        print('YES')
    else:
        print('NO')