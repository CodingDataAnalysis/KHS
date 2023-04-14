import math, sys
input = sys.stdin.readline().rstrip

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    print(gcd * A)
    print(gcd * B)
