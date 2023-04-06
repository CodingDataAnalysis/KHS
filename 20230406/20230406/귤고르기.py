from collections import Counter

tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 6

tangerine_tuple = Counter(tangerine).most_common()

tmp = 0
result = 0
for i, tuple in enumerate(tangerine_tuple, 1):
    tmp += tuple[1] 
    if tmp >= k:
        result = i
        break
print(result)