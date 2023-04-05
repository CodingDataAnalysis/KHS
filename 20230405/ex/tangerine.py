from collections import Counter
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 6

# 수확한 귤 중 k개를 골라서 숫자별로 분류
# 서로 다른 종류가 최소로 하는 방법

counter = Counter(tangerine).most_common()
