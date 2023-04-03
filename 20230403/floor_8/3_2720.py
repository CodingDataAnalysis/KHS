change = {'Quater':25, 'Dime':10, 
          'Nickel':5, 'Penny':1}

T = int(input())
for i in range(T):
    C = int(input())
    change_list = []
    while C > 0:
        change_list.append(C//change['Quater'])
        C = C%change['Quater']
        change_list.append(C//change['Dime'])
        C = C%change['Dime']
        change_list.append(C//change['Nickel'])
        C = C%change['Nickel']
        change_list.append(C//change['Penny'])
        C = C%change['Penny']
    print(*change_list)