import sys

N = int(sys.stdin.readline())
num_list = [0 for _ in range(10001)]

for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
            for k in range(num_list[i]):
                print(i)