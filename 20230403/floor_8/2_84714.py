n,b = map(int,(input().split()))

result = []
while n:
    # 자릿수 계산 결과가 10보다 커서 알파벳으로 나타내야하는 경우
    if n%b >= 10:
        result.append(chr(n%b+ord('A')-10))
    else:
        result.append(n%b)
    n //= b
    
# 1의 자릿수가 result의 0번째 요소부터
# 추가되므로 역정렬한 값을 문자열로 변환해 출력
print(''.join(map(str,result[::-1])))