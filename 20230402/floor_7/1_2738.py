N, M = map(int, input().split())
list_1, list_2 = [], []
for i in range(N):
    list_1.append([num for num in map(int, input().split())])
for i in range(N):
    list_2.append([num for num in map(int, input().split())])

result = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        result[i][j] = list_1[i][j] + list_2[i][j]

for i in result:
    print(*i)
