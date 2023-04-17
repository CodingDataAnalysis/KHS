from itertools import count
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = set([input().rstrip() for _ in range(n)])
count = 0

for i in range(m):
    m_list = input().rstrip()
    if m_list in n_list:
        count += 1
print(count)