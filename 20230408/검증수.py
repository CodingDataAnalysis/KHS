sum_sqrt = 0
serial_list = [num for num in map(int, input().split())]
for i in serial_list:
    sum_sqrt += i**2
print(sum_sqrt%10)