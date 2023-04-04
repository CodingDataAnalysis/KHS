# 네 번째 점

coords_list =  [list(map(int, input().split())) for _ in range(3)]
x_list, y_list = [], []
for coords in coords_list:
    x_list.append(coords[0])
    y_list.append(coords[1])
for x in x_list:
    if x_list.count(x) == 1:
        result_x = x
for y in y_list:
    if y_list.count(y) == 1:
        result_y = y
print(result_x, result_y)