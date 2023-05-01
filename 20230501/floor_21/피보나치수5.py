N = int(input())

def fibonachi(N:int):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibonachi(N-2) + fibonachi(N-1)

print(fibonachi(N))
