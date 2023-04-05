# 수학은 비대면강의입니다.
# 정수 a, b, c, d, e, f 를 받아서
# ax + by = c
# dx + ey = f
# 두 방정식을 만족하게 하는 x, y값을 출력하라

a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break