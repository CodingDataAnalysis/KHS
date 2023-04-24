from sys import stdin
input = stdin.readline

N, K = map(int, input().rstrip().split())
n_list = [n for n in range(1, N+1)]
c = []
while n_list:
    c.append(n_list.pop(K-1))
    
