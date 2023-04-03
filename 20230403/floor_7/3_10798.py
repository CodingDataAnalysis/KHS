strings = []
for i in range(5):
    string = input()
    strings.append(string)

max_len = len(max(strings, key=len))
output = ''

for i in range(max_len):
    for j in range(5):
        if i < len(strings[j]):
            output += strings[j][i]
print(output)