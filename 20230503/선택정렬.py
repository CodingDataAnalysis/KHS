def selection_sort(arr, l , r):
    global K
    count = 0
    for i in range(r, l-1, -1):
        tmp = arr[:i+1]
        if arr[i] != max(tmp):
            answer = arr[i], max(tmp)
            arr[arr.index(max(tmp))], arr[i] = answer
            count += 1
            if count == K:
                return count, answer
    return count, -1

A, K = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = len(arr) - 1

count, answer = selection_sort(arr, l, r)
if count < K:
    print(answer)
else:
    print(*answer)