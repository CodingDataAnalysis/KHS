# ㅁ  ㅁ
# ㅁ  ㅁ
# ㅁ  ㅁ
# 양쪽에 3지점씩 있을 때,
# 각 다리끼리 겹쳐질 수 없다고 할 때
# 다리를 지을 수 있는 경우의 수를 구하라.
# N <= M

from math import factorial
f = factorial
t= int(input())
for i in range(t):
    n, m = map(int, input().split())
    bridge = f(m) // (f(n) * f(m - n))
    print(bridge)