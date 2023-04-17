a, b = map(int, input().split())
res = a*b

# 유클리드 호제법
while b:
    if a > b:
        a, b = b, a
    b = b % a

print(res//a)
