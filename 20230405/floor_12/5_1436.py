# 영화감독 숌
# 정수 N을 받는다.
# N 번째 영화의 제목에 666이 들어가면 그 수를 출력

N = int(input())
satan_list = []
i = 665

for i in range(666, 2666800):
    if '666' in str(i):
        satan_list.append(i)
        if len(satan_list) == N:
            print(satan_list[-1])
            break


