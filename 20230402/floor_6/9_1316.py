N = int(input())
counter = 0
for i in range(N):
    S = input()
    isGroupedWord = True
    for j in set(s for s in S):
        if j*S.count(j) not in S:
            isGroupedWord = False
    if isGroupedWord:
        counter += 1
print(counter)
