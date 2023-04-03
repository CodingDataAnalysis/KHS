n, b = input().split()
b = int(b)

result = 0
exponent = len(n) - 1
for digit in n:
    if digit.isalpha():
        result += (ord(digit) - ord('A') + 10) * (b ** exponent)
    else:
        result += int(digit) * (b ** exponent)
    exponent -= 1

print(result)

# 10진법에서 A~Z는 10~35에 대응
# ord()로 ascii 변환한 숫자에 ord('A') + 10을 빼면
# ascii에서도 정수가 1씩 증가하므로 문자의 10진법 변환한 수가 됨