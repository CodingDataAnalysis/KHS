N = int(input())
scores = [num for num in map(int, input().split())]
scores = list(map(lambda score: score/max(scores)*100, scores))
print(sum(scores)/len(scores))