#    n!          ==      n
# k! * (n-k)!            k

from math import factorial

n, k = map(int, input().split())
f = factorial
print(f(n) // (f(k)*f(n-k)))