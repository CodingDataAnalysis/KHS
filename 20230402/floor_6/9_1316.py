N = int(input())
for i in range(N):
    S = input()
    counter = 0
    for j in set(s for s in S):
        isGroupedword = True
        if j*S.count(j) not in S:
            isGroupedWord = False
        
print(counter)
