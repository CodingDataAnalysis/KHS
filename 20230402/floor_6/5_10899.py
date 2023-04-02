import sys
S = sys.stdin.readline().rstrip()

if S == S[::-1]:
    print(1)
else: print(0)