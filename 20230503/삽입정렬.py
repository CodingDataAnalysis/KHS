def insertion_sort(arr, l, r):
    global K
    count = 0
    for i in range(l+1, r+1):
        idx = 0
        for j in range(i, -1, -1):
            target = arr[j]
            try:
                if arr[j] < arr[j-1]:
                    answer = arr[j-1]
                    arr[j] = answer
                    count += 1
                    if count == K:
                        return answer
            except: 
                pass
            if j == 0 or target > arr[j]:
                arr[j] = answer = target
                count += 1
                if count == K:
                    return answer
            else:
                break
    return count, -1


from sys import stdin
input = stdin.readline

A, K = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, len(arr)-1

count, answer = insertion_sort(arr, l, r)
print(count, answer)