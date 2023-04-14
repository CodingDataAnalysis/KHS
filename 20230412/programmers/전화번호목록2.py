phone_book = ["119", "97674223", "1195524421"]
phone_book = sorted(phone_book)
answer = True

for i, j in zip(phone_book, phone_book[1:]):
    if j.startswith(i):
        answer = False
        break
print(answer)