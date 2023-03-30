N, M = map(int, input().split())

baskets = [0 for _ in range(N)]

for n in range(M):
    i, j, k = map(int, input().split())
    for m in range(i-1, j):
        baskets[m] = k

for basket in baskets:
    print(basket, end=' ')