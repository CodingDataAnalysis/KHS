def weird_sign(A, B):
    return (A+B)*(A-B)

A, B = map(int, input().split())
print(weird_sign(A, B))