num_list = []
max_num = -1
index = [0, 0]
for i in range(9):
    num_list.append([num for num in map(int, input().split())])
    if max(num_list[i]) > max_num:
        max_num = max(num_list[i])
        index = [i+1, num_list[i].index(max_num)+1]
print(max_num)
print(*index)