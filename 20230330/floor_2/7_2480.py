def three_dice():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        return print(10000 + a * 1000)
    elif a == b:
        return print(1000 + a * 100)
    elif b == c:
        return print(1000 + b * 100)
    elif c == a:
        return print(1000 + c * 100)
    else:
        return print(max([a, b, c]) * 100)
    

if __name__ == "__main__":
    three_dice()

