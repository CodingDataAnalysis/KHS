def cantor(N):
    if N == 0:
        return '-'
    pre = cantor(N-1)
    new = pre + ' ' * len(pre) + pre
    return new

while True:
    try:
        N = int(input())
        print(cantor(N))
    except:
        break