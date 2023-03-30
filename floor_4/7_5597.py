student_list = list(range(1, 31))

checked_list = []
for i in range(28):
    checked_list.append(int(input()))

sorted_checked_list = sorted(checked_list)

for s1 in student_list:
    if s1 not in sorted_checked_list:
        print(s1)