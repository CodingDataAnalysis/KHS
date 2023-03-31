N = int(input())
stars = 2*N-1

for i in range(1, N+1):
    print(' '*(N-i), '*'*(i*2-1), sep='')
for i in range(1, N):
    print(' '*(i), '*'*(stars-i*2), sep='')