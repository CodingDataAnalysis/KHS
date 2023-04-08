student_list = list(range(1, 31))
no_submit = []

for i in range(30):
    student_number = int(input())
    if student_number not in student_list:
        no_submit.append(student_number)

print(sorted(no_submit))