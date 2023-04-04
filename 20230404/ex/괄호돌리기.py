def check_brakets(s):
    stack = []
    counter = 0

    for ch in s:
        if ch in ['(', '{', '[']:
            stack.append(ch)
        else:
            if not stack:
                counter += 1
            elif stack[-1] == '(' and ch == ')':
                stack.pop()
            elif stack[-1] == '{' and ch == '}':
                stack.pop()
            elif stack[-1] == '[' and ch == ']':
                stack.pop()

    if not stack and counter == 0:
        return True
    else:
        return False
    

def solution():
    s = input()
    result = 0
    for _ in range(len(s)):
        if check_brakets(s):
            result += 1
        else:
            pass
        s_list = list(s)
        s_list.append(s_list.pop(0))
        s = ''.join(s_list)
    return result

if __name__ == "__main__":
    print(solution())