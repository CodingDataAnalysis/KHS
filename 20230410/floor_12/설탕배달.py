N = int(input())

if N in [1, 2, 4, 7]:
    print(-1)
    exit()

if N % 5 == 0:
    print(N // 5)
else:
    M = N // 5
    N = N % 5
    if N % 3 == 0:
        print(M + (N // 3))
    elif N % 3 == 1:
        print(M + (N // 3) + 1)
    elif N % 3 == 2:
        print(M + (N // 3) + 2)
    else:
        print(-1)
