num_list = [int(input()) for _ in range(5)]

print(sum(num_list) // len(num_list))
num_list.sort()
print(num_list[2])
