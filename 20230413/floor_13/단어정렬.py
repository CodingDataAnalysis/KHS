n = int(input())
string_list = [[0] for _ in range(n)]
for i in range(n):
    string_list[i] = input()

string_list = list(set(string_list))
string_list.sort(key=lambda x: (len(x), ascii(x)))

print(*string_list, sep='\n')