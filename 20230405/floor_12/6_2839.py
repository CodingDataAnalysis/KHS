N = int(input())

if N in [4, 7]:
    print(-1)

if N % 5 == 0:
    print(N//5)
else:
    if N % 5 == 1:
        print(N//5-1+2)
    elif N % 5 == 2:
        print(N//5-2+4)
    elif N % 5 == 3:
        print(N//5+1)
    elif N % 5 == 4:
        print(N//5-1+3)
    else:
        print(-1)
