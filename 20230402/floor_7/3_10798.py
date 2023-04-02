char_list = []
for i in range(5):
    char_list.append([char for char in input()])
p = len(max(char_list, key=len))
result = ''
for i in range(p):
    for j in range(p):
        try:
            result += char_list[j][i]
        except:
            pass
print(result)