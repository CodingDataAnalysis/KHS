N, X = map(int, input().split())
A = input().split()

numList = []
for num in A:
    numList.append(int(num))

for num in numList:
    if num < X:
        print(num, end=' ')