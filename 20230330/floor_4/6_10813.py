N, M = map(int, input().split())

baskets = [num for num in range(1, N+1)]

for n in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    baskets[j], baskets[i] = baskets[i], baskets[j]

for basket in baskets:
    print(basket, end=' ')