from collections import deque
import sys

N = int(sys.stdin.readline())
num_list = deque([int(sys.stdin.readline()) for _ in range(N)])
print(*sorted(num_list), sep='\n')