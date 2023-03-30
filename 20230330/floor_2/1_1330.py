def comparsion_two_number():
    a, b = input().split()
    a, b = int(a), int(b)
    if a > b:
        return print('>')
    elif a < b:
        return print('<')
    elif a == b:
        return print('==')
    

if __name__ == '__main__':
    comparsion_two_number()