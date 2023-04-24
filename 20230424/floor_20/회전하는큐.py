from collections import deque

N, M = map(int, input().split())

queue = deque(range(1, N+1))
target = deque(list(map(int, input().split())))
count = 0

while target:
    if queue[0] == target[0]:
        queue.popleft()
        target.popleft()
    else:
        if queue.index(target[0]) <= len(queue)//2:
            queue.append(queue.popleft())
            count += 1
        else:
            queue.appendleft(queue.pop())
            count += 1
print(count)
    
