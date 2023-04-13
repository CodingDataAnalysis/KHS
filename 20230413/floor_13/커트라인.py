# 응시자 수 N, 수상자 수 k, 점수 목록 x

N, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort(reverse=True)
print(x[:k].pop())