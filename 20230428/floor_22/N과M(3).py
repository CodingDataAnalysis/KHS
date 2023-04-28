N, M = map(int, input().split())
result = []

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        result.append(i)
        dfs(depth+1)
        result.pop()

dfs(0)
print(*result)
