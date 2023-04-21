# 점이 3개일 때, 1개 점을 중심으로 나머지 점 2개가 추가되는 방식
# 최종 점의 개수를 구한 다음 제곱(사각형이므로)한 값을 구하면 됨

n = int(input())
point = 2
for i in range(n):
    point = point + point -1
print(point*point)