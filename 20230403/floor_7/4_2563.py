zero_square = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())
counter = 0
for i in range(N):
    Y, X = map(int, input().split())
    for x in range(X, X+10):
        for y in range(Y, Y+10):
            zero_square[x][y] = 1

for i in zero_square:
    counter += i.count(1)
print(counter)
