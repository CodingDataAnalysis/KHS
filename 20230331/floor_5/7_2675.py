import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    R, S = sys.stdin.readline().split()
    S = S.rstrip()
    R = int(R)
    for char in S:
        print(char*R, end='')
    print()