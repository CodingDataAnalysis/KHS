from sys import stdin
from collections import deque
input = stdin.readline
t= int(input())

for i in range(t):
    n, m = map(int, input().rstrip().split())
    docs = list(map(int, input().rstrip().split()))
    max_ = max(docs)
    print(docs[n+1 % max_])