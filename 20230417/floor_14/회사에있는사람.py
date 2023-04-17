import sys
input = sys.stdin.readline
n = int(input())
employee = dict()

for i in range(n):
    name, isEnter = input().rstrip().split()
    if isEnter == 'enter':
        employee[name] = isEnter
    else:
        del employee[name]

employee = sorted(employee.keys(), reverse=True)

print(*employee)