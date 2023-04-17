from math import sqrt
m, n = map(int, input().split())

arr = [True]*(n+1)
arr[0:2] = False, False
for i in range(m, int(sqrt(n))+1):
    j = 2
    if arr[i]:
        while True:
            if i*j > len(arr)-1:
                break
            arr[i*j] = False
            j += 1

sum = 0
for i in range(m, n+1):
    if arr[i]:
        sum += 1
        print(i)
