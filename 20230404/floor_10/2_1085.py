# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
x_min, y_min = 0, 0

if x <= w-x:
    x_min = x
else:
    x_min = w-x

if y <= h-y:
    y_min = y
else:
    y_min = h-y

print(min([x_min, y_min]))