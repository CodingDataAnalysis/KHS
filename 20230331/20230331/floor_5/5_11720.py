import sys

N = sys.stdin.readline().rstrip()
num_string = sys.stdin.readline().rstrip()

sum = 0
for num in num_string:
    sum += int(num)

print(sum)