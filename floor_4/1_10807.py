N = int(input())
int_list = []
int_string = input()
v = int(input())

for int_ in int_string.split():
    int_list.append(int(int_))

print(int_list.count(v))