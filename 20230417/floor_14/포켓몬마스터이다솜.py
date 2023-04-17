import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
name_dict = dict()
num_dict = dict()

for num in range(1, N+1):
    data = input().rstrip()
    name_dict[data] = num
    num_dict[num] = data

for m in range(M):
    data = input().rstrip()
    if data.isdigit():
        print(num_dict[int(data)])
    else:
        print(name_dict[data])