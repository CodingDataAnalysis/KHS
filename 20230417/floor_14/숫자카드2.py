from sys import stdin
from collections import Counter
input = stdin.readline

N = input().rstrip()
n_cards = list(map(int, input().rstrip().split()))
n_counter = Counter(n_cards)
M = input().rstrip()
m_cards = list(map(int, input().rstrip().split()))

for i in range(len(m_cards)):
    if m_cards[i] in n_counter:
        print(n_counter[m_cards[i]], end=' ')
    else:
        print(0, end=' ')