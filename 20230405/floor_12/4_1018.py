# 체스판 다시 칠하기

N, M = map(int, input().split())
board = [str(input()) for _ in range(N)]
target = 0
# 짝수 길이인 경우 시작과 끝 문자가 달라야 함
if M % 2 == 0:
    sep = int(M/2)
    for line in board:
        if line[0] == 'W':
            cnt_wb = line.count('WB')
            cnt_bw = line.count('BW')
            cnt_w = line.count('W')
            cnt_b = line.count('B')
            if cnt_wb == sep:
                continue
            elif cnt_w > sep:
                if cnt_w % 2 != 0:
                    target += cnt_w - cnt_wb - 1
                else:
                    target += cnt_w - sep
        else:
            if cnt_bw == sep:
                continue
            elif cnt_b > sep:
                if cnt_b % 2 != 0:
                    target += cnt_b - sep - 1
                else:
                    target += cnt_b - sep
print(target)
