from sys import stdin
from collections import Counter

n = int(stdin.readline())
lst = [int(stdin.readline()) for _ in range(n)]
lst.sort()

counter = Counter(lst).most_common()
most_freq = 0

if len(counter) == 1:
    most_freq = counter[0][0]
elif counter[0][1] == counter[1][1]:
    most_freq = counter[1][0]
else:
    most_freq = counter[0][0]

print(round(sum(lst)/len(lst)))
print(lst[len(lst)//2])
print(most_freq)
print(lst[-1] - lst[0])