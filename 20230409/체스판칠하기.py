import sys
input = sys.stdin.readline
from collections import defaultdict

N, M=map(int, input().split())
board=[list(input().rstrip()) for x in range(N) ]
T=defaultdict(int)
for i in range(N-7):
    for j in range(M-7):
        for x in range(i,i+8):
            for y in range(j,j+8):
                if ((x+y)%2==0 and board[x][y]=='B') or ((x+y)%2==1 and board[x][y]=='W'):
                    T[str(i)+str(j)]+=1
                    a = T[str(i)+str(j)]
                T[str(i)+str(j)] = min(a,64-a)
print(min(T.values()))