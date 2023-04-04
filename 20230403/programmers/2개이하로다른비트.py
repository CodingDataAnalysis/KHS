X = int(input())
bit = str(bin(X)[2:])

if len(bit) < 4:
    while len(bit) == 4:
        bit = '0'.join(bit)
print(bit)
