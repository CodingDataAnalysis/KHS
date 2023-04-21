from sys import stdin
input = stdin.readline
while True:
    str_stack = ''
    s = input().rstrip()
    if s == '.':
        break
    for char in s:
        if char in '()[]':
            str_stack += char
    if len(str_stack) == 0:
        print('yes')
    elif len(str_stack) % 2 != 0:
        print('no')
    else:
        for i in range(len(str_stack)//2):
            str_stack = str_stack.replace("()", "")
            str_stack = str_stack.replace("[]", "")
        if len(str_stack) == 0:
            print('yes')
        else:
            print('no')