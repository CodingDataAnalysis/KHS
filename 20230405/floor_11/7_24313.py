a1, a0 = map(int, input().split())
C = int(input())
n = int(input())

if a1*n+a0 <= C*n and C >= a1:
    print(1)
else:
    print(0)