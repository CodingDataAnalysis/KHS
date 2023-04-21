K = int(input())
stack = list()
for k in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

try:
    print(sum(stack))
except:
    print(0)