from math import gcd
n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())
n = n1 * d2 + n2 * d1
d = d1 * d2
g = gcd(max(n, d), min(n, d))
print(n//g, d//g)