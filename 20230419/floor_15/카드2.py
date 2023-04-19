from collections import deque
from sys import stdin
N_cards = deque(range(1, int(stdin.readline())+1))
while len(N_cards) > 1:
    N_cards.popleft()
    N_cards.append(N_cards.popleft())
print(N_cards.pop())