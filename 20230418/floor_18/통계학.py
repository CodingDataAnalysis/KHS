from collections import Counter
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

print(round(sum(lst)/len(lst)))
print(list(sorted(set(lst)))[len(lst)//2+1])
print(list(Counter(lst).keys())[0])
print(max(lst)- min(lst))
