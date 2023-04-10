N = int(input())
if N % 5 == 0:
    print(N//5)
else:
    N = N // 5
    if N % 3 == 0:
        print(N + (N//3))
    else:
        print(-1)