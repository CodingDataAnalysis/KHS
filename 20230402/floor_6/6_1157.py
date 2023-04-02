import sys, collections

word = sys.stdin.readline().rstrip().upper()

max_dict = collections.Counter(word)

if list(max_dict.values()).count(max(max_dict.values())) >= 2:
    print('?')
else: 
    print(list(max_dict.keys())[list(max_dict.values()).index(max(max_dict.values()))])
    