def calculator():
    a, b = input().split()
    a, b = int(a), int(b)
    return print(a+b, a-b, a*b, a//b, a%b, sep='\n')

if __name__ == "__main__":
    calculator()