def cal_comparsion():
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    return print((a+b)%c, ((a%c) + (b%c))%c, 
                 (a*b)%c, ((a%c) * (b%c))%c, sep='\n')

if __name__ == "__main__":
    cal_comparsion()