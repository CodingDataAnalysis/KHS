from sys import stdin

arr = [False, False] + [True]*(999999)
for i in range(len(arr)):
    if arr[i]:
        for j in range(2*i, len(arr), i):
            arr[j] = False

T = int(stdin.readline())
for i in range(T):
    n = int(stdin.readline())
    count = 0
    for j in range(2, n//2+1):
        if arr[j] and arr[n - j]:
            count += 1
    print(count)