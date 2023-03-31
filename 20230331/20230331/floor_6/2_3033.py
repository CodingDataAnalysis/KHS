black_piece = [1, 1, 2, 2, 2, 8]
white_piece = [int(num) for num in input().split()]

for i in range(len(white_piece)):
    print(black_piece[i] - white_piece[i], end=' ')