import sys
S = sys.stdin.readline().rstrip()

alphabet_ascii_list = range(ord('a'), ord('z')+1)
alphabet_list = [chr(i) for i in alphabet_ascii_list]

for alphabet in alphabet_list:
    if alphabet in S:
        print(S.index(alphabet), end=' ')
    else:
        print('-1', end=' ')
    