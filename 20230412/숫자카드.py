import sys
input = sys.stdin.readline

N = int(input())
N_cards = set(map(int, input().rstrip().split()))
M = int(input())
M_cards = list(map(int, input().rstrip().split()))

for card in M_cards:
    if card in N_cards:
        print(1, end=' ')
    else:
        print(0, end=' ')

N_cards.union(M_cards)