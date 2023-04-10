from collections import deque
import sys

max_num = 0
tmp_list = deque()

for i in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    tmp_list.append(num)

for i in range(len(tmp_list)):
    for j in range(i, len(tmp_list)):
        if tmp_list[i] > tmp_list[j]:
            tmp_list[i], tmp_list[j] = tmp_list[j], tmp_list[i]

print(*tmp_list, sep='\n')