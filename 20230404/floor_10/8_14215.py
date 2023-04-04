# 세 막대

A, B, C = map(int, input().split())
aspect_list = [A, B, C]
max_value = max(aspect_list)
aspect_list.remove(max_value)
if max_value >= sum(aspect_list):
    max_value = sum(aspect_list) - 1
print(max_value + sum(aspect_list))