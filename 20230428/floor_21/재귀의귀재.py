def recursion(S:str, l:int, r:int):
    if l >= r:
        return (1, l+1)
    elif S[l] != S[r]:
        return (0, l+1)
    else:
        return recursion(S, l+1, r-1)
    
def isPalindrome(S):
    return recursion(S, 0, len(S)-1)


T = int(input())
for i in range(T):
    S = input()
    print(*isPalindrome(S))
