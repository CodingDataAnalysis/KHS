T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    docs = [(value, index) for value, index in enumerate(docs)]
    count = 0

    while True:
        if max(docs)[0] == docs[0][0]:
            count += 1
            if docs[0][1] == m:
                print(count)
                break
            else:
                docs.pop(0)
        else:
            docs.append(docs.pop(0))