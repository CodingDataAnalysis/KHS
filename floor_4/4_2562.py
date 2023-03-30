num_list = []
for i in range(1, 10):
    num_list.append(int(input()))

max_num = max(num_list)
print(max_num, num_list.index(max_num) + 1, sep='\n')