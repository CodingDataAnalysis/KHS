import heapq

phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    phone_book = list(map(int, phone_book))
    answer = True
    while phone_book:
        a = heapq.heappop(phone_book)
        for i in phone_book:
            if str(a) in str(i):
                answer = False
                return answer
    return answer

print(solution(phone_book=phone_book))