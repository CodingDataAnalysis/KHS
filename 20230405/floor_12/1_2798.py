# 블랙잭
# N 개 카드의 중에서 3개를 이용하여 
# M을 넘지 않으면서 최대한 가까운 숫자 조합 만들기

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
blackJack = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_total = sum([card_list[i], card_list[j], card_list[k]])
            if blackJack <= card_total < M:
                blackJack = card_total
            elif card_total == M:
                blackJack = card_total
                break
            else:
                pass
print(blackJack)