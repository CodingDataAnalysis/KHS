# 삼각형 외우기

aspect_list = [int(input()) for _ in range(3)]

if aspect_list[0] == aspect_list[1] and \
    aspect_list[0] == aspect_list[2] and \
    aspect_list[1] == aspect_list[2]:
    print('Equilateral')
elif sum(aspect_list) == 180:
    if aspect_list[0] == aspect_list[1] or \
    aspect_list[0] == aspect_list[2] or \
    aspect_list[1] == aspect_list[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')