from collections import deque

progresses = [93, 30, 55]
speeds = [1, 30 , 5]

delay_list = deque()
for i in range(len(progresses)):
    delay = 100 % progresses[i] 
    if delay <= speeds[i]:
        delay_list.append(1)
    else:
        delay_list.append(delay // speeds[i])

result = []
count = 0
max_ = delay_list.popleft()
while delay_list:
    temp = delay_list.popleft()
    if max_ < temp:
        max_ = temp
        count = 1
        result.append(count)
    else:
        count += 1
        continue
print(result)
