total_score = 0
total_avg = 0.
for i in range(20):
    subject, score, rank = input().split()
    if rank == 'A+':
        total_avg += float(score)*4.5
        total_score += float(score)
    elif rank == 'A0':
        total_avg += float(score)*4.
        total_score += float(score)
    elif rank == 'B+':
        total_avg += float(score)*3.5
        total_score += float(score)
    elif rank == 'B0':
        total_avg += float(score)*3.
        total_score += float(score)   
    elif rank == 'C+':
        total_avg += float(score)*2.5
        total_score += float(score)
    elif rank == 'C0':
        total_avg += float(score)*2.
        total_score += float(score)
    elif rank == 'D+':
        total_avg += float(score)*1.5
        total_score += float(score)
    elif rank == 'D0':
        total_avg += float(score)*1.
        total_score += float(score)
    elif rank == 'F':
        total_avg += float(score)*0.
        total_score += float(score)
    else: pass
print(total_avg/total_score)

