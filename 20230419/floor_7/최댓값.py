n = m = 9
max_ = -1
coords = {'x':'', 'y':''}

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    if max_ < max(arr):
        max_ = max(arr)
        coords['x'] = i
        coords['y'] = arr.index(max_) + 1

print(max_)
print(coords['x'], coords['y'])
