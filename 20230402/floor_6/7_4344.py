C = int(input())

for i in range(C):
    score_list = [s for s in map(int, input().split())]
    N = score_list.pop(0)
    avg = sum(score_list)/N
    avg_over_count = 0
    for s1 in score_list:
        if s1 > avg:
            avg_over_count += 1
    print(f'{avg_over_count/N*100:.3f}%')