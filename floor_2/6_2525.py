def oven_timer():
    H, M = map(int, input().split())
    oven_time = int(input())
    

    if M + oven_time >= 60:
        H += (M + oven_time) // 60
        M = (M + oven_time) % 60
        if H == 24:
            H = 0
        elif H > 24:
            H = H % 24
        if M == 60:
            M = 0
        elif M > 60:
            M = M % 60
    else:
        M += oven_time

    return print(H, M)

if __name__ == "__main__":
    oven_timer()