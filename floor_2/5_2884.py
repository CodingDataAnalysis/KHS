def alram_already():
    H, M = map(int, input().split())
    if M <= 44:
        M = M + 15
        if H == 0:
            H = 23
        else: 
            H = H - 1
    elif M >= 45:
        M = M - 45
    return print(H, M)


if __name__ == "__main__":
    alram_already()
