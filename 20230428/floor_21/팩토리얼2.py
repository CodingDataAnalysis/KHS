def factorial(N:int):
    if N <= 1:
        return 1
    return N * factorial(N-1)
    
N = int(input())
print(factorial(N))