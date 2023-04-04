# 삼각형과 세 변

while True:
    A, B, C = map(int, input().split())
    aspect_list = [A, B, C]
    if aspect_list == [0, 0, 0]:
        break
    max_value = max(aspect_list)
    aspect_list.remove(max_value)
    if max_value < sum(aspect_list):
        if A == B and B == C:
            print('Equilateral')
        elif A == B or A == C or B == C:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')