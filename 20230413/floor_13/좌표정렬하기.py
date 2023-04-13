import sys

N = int(sys.stdin.readline())
x_list, y_list = [[0] for _ in range(N)], [[0] for _ in range(N)]

for i in range(N):
    x_list[i], y_list[i] = map(int, sys.stdin.readline().rstrip().split())

coords = [[x, y] for x, y in zip(x_list, y_list)]
coords.sort()

for x, y in coords:
    print(x, y)