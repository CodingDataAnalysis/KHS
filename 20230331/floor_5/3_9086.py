import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    S = sys.stdin.readline().rstrip()
    if S.isdigit():
        pass
    else:
        print(S[0], S[-1], sep='')