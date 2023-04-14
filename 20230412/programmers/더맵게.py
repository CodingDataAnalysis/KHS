import heapq

K = 7
scoville = [1, 2, 3, 9, 10, 12]

def solution(K, scoville):
    heapq.heapify(scoville)
    combine = 0
    count = 0

    while len(scoville) > 1 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        combine += a + b * 2
        count += 1
        heapq.heappush(scoville, combine)
        if combine >= K:
            return count
    return count

print(solution(K=K, scoville=scoville))
