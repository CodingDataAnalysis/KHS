# 분해합
# 114의 생성자는 111 + 1 + 1 + 1 이므로 111이 성립
# 자연수 n과 자연수n의 각 자릿수를 합하여 자연수 m이 성립하면
# 자연수 n은 m의 생성자라고 한다.

n = int(input())
creater_list = []
for k in range(n):
    k_list = [int(ch) for ch in str(k)]
    if k + sum(k_list) == n:
        creater_list.append(k)
if not creater_list:
    print(0)
else:
    print(min(creater_list))
