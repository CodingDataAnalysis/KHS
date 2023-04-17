# 듣도못한사람수, 보도못한사람수 = map(int, input().split())
듣도못한사람수, 보도못한사람수 = 3, 4

# 듣도못한사람목록 = set([input() for _ in range(듣도못한사람수)])
듣도못한사람목록 = set(['ohhenrie', 'charlie', 'baesangwook'])

# 보도못한사람목록 = set([input() for _ in range(보도못한사람수)])
보도못한사람목록 = set(['obama', 'baesangwook', 'ohhenrie', 'clinton'])

듣보잡 = 듣도못한사람목록.intersection(보도못한사람목록)
print(len(듣보잡), *sorted(듣보잡), sep='\n')