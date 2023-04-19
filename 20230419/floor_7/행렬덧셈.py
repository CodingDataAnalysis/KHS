from sys import stdin
input = stdin.readline
n, m = map(int, input().rstrip().split())
arr_1 = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr_2 = [list(map(int, input().rstrip().split())) for _ in range(n)]
sum_arr = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        sum_arr[i][j] = arr_1[i][j] + arr_2[i][j]

for sum in sum_arr:
    print(*sum)