def prime_sieve(n):
    sieve = (1 << (n + 1)) - 1  # 비트마스크 초기화
    sieve &= ~(0b1 | 0b10)  # 0과 1은 소수가 아니므로 제외
    for i in range(2, int(n ** 0.5) + 1):  # 2~n^(1/2)까지 반복
        if sieve & (1 << i):  # i가 소수인 경우
            sieve &= ~(1 << (i * j) for j in range(2, (n // i) + 1))  # i의 배수들을 모두 소수에서 제외
    return [i for i in range(2, n + 1) if sieve & (1 << i)]  # 소수만 리스트로 반환


print(prime_sieve(int(input())))