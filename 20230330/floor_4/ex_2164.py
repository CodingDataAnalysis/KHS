cards = list(range(1, int(input())+1))
while cards:
    cards.pop(0)
    cards.append(cards.pop(0))
    print(cards)
    if len(cards) == 1:
        break

print(cards)