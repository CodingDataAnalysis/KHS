# 대지

N = int(input())
coords_list =  [list(map(int, input().split())) for _ in range(N)]
x_list, y_list = [], []
for coords in coords_list:
    x_list.append(coords[0])
    y_list.append(coords[1])
x_max = max(x_list)
x_min = min(x_list)
y_max = max(y_list)
y_min = min(y_list)
print((x_max - x_min) * (y_max - y_min))