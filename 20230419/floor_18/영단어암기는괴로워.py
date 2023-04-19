# 자주 나오는 단어일수록 앞으로
# 단어 길이가 길수록 앞으로
# 사전 순으로 앞에 있을수록 앞으로
# N = 단어 개수
# M = 단어 길이 기준
# M 기준을 만족하는 단어에 대해서만 처리함
# [단어 개수, 단어 길이, 단어] 가 담긴 이중배열을 값에 따라 정렬
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
wordbook = dict()

for _ in range(n):
    word = stdin.readline().rstrip()
    if len(word) < m:
        continue
    if word not in wordbook:
        wordbook[word] = [1, len(word), word]
    else:
        wordbook[word][0] += 1

word_list = list(wordbook.values())
word_list.sort(key=lambda x: (-x[0], -x[1], x[2]))
result = list(map(lambda x: x[2], word_list))
print(*result)