import sys
S = sys.stdin.readline().rstrip()
req_time = 0
for s in S:
    if s in ['A', 'B', 'C']:
        req_time += 3
    elif s in ['D', 'E', 'F']:
        req_time += 4
    elif s in ['G', 'H', 'I']:
        req_time += 5
    elif s in ['J', 'K', 'L']:
        req_time += 6
    elif s in ['M', 'N', 'O']:
        req_time += 7
    elif s in ['P', 'Q', 'R', 'S']:
        req_time += 8
    elif s in ['T', 'U', 'V']:
        req_time += 9
    elif s in ['W', 'X', 'Y', 'Z']:
        req_time += 10
    else: pass
print(req_time)
