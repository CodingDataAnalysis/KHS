def bubble_sort(arr, l, r):
    global K
    count = 0
    for i in range(r, l, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                answer = arr[j+1], arr[j]
                arr[j], arr[j+1] = answer
                count += 1
                if count == K:
                    return count, answer
    return count, -1


from sys import stdin
input = stdin.readline

A, K = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = len(arr) - 1

count, answer = bubble_sort(arr, l, r)
if count < K:
    print(answer)
else:
    print(*answer)

# 1회 : 전체 요소 중 최대값을 뒤로 이동시키면서 정렬
# 2회 : 정렬된 부분을 제외한 나머지 요소 중에서
#  최대값을 뒤로 이동시키면서 정렬렬