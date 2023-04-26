progresses = [33, 40, 99, 1, 63, 1]	
speed = [3, 15, 1, 21, 8, 50]

import math
from collections import deque

def solution(progresses, speed):
    lead = []
    for p in range(len(progresses)):
        lead.append(math.ceil((100 - progresses[p]) / speed[p]))
    print(lead)
    stack = deque()
    answer = []
    for i in lead:
        if len(stack) == 0:
            stack.append(i)
        else:
            if max(stack) >= i:
                stack.append(i)
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(i)
    if stack:
        answer.append(len(stack))
    return answer

print(solution(progresses, speed))
