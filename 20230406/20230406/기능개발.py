import math

progresses = [1, 99, 49, 91, 10, 99]
speeds = [30, 1, 12, 2, 22, 1]

delay_list = []
for i in range(len(progresses)):
    n = 100 - progresses[i]
    delay = math.ceil(n / speeds[i])
    delay_list.append(delay)

print(delay_list)

deploy_list = []
deploy_num = 1
maximum = delay_list.pop(0)

for number, i in enumerate(delay_list, 1):
    if maximum >= i:
        deploy_num += 1
        if number == len(delay_list):
            deploy_list.append(deploy_num)
    else:
        deploy_list.append(deploy_num)
        deploy_num = 1
        maximum = i
        if number == len(delay_list):
            deploy_list.append(deploy_num)
        
print(deploy_list)