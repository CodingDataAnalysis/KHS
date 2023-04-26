# () [] {} 은 올바른 문자열
# ( A ) 는 올바른 문자열
# { A ) 는 틀린 문자열
# 문자열 s가 주어졌을 때
# 왼쪽으로 회전을 문자열의 길이만큼 반복한다.
# 매 반복마다 올바른 문자열이 성립하면 answer를 1 증가시킨다.

from collections import deque
from sys import stdin
input = stdin.readline

s = "}}}"

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        print(s)
        stack = deque()
        f1 = True
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if len(stack) > 0:
                    if stack[-1] == "(" and char == ")":
                        stack.pop()
                    elif stack[-1] == "[" and char == "]":
                        stack.pop()
                    elif stack[-1] == "{" and char == "}":
                        stack.pop()
                else:
                    f1 = False
                    break
        if not stack and f1:
            answer += 1
        s.append(s.popleft())
    return answer

print(solution(s))