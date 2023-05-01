# 입력 배열에 대해 길이를 중간지점으로 나누고
# start ~ median 까지 정렬
# median+1 ~ end까지 정렬
# 두 결과를 병합
# 재귀로 작성

A, K = map(int, input().split())
arr = list(map(int, input().split()))
p, r = 0, A-1
count, answer = 0, 0

def merge_sort(arr, p, r):
    global count, K
    if p < r and count <= K:
        q = (p+r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global count, answer, K
    i, j, = p, q+1
    tmp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1

    i, t = p, 0
    while i <= r:
        arr[i] = tmp[t]
        count += 1
        if count == K:
            answer = arr[i]
            break
        i, t = i+1, t+1

merge_sort(arr, p, r)
if count < K:
    print(-1)
else:
    print(answer)