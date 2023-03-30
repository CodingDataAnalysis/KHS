def choose_quater():
    x = int(input())
    y = int(input())

    if x > 1 and y > 1: print(1)
    elif x < 0 and y > 1: print(2)
    elif x < 0 and y < 0: print(3)
    elif x > 1 and y < 0: print(4)


if __name__ == "__main__":
    choose_quater()