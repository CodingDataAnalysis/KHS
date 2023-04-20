import heapq

jobs = [[0, 3], [1, 9], [2, 6]]
modified = list(map(lambda x: x[1], jobs))
heapq.heapify(modified)

sum_ = 0
discnt = 0
dict_ = dict()
while modified:
    sum_ += heapq.heappop(modified)
    dict_[sum_] = sum_ - discnt
    discnt += 1

answer = sum(dict_.values()) // len(dict_.values())
print(answer)
    
