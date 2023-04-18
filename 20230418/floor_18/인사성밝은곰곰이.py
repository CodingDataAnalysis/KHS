from sys import stdin
N = int(stdin.readline())

count = 0
tmp = 0
used_gomgom = set()
for n in range(N):
    s = stdin.readline().rstrip()
    if s == 'ENTER':
        used_gomgom.clear()
        count += tmp
        tmp = 0
    elif s in used_gomgom:
        continue
    else:
        used_gomgom.add(s)
        tmp += 1
count += tmp
print(count)