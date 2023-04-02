word = input()
target_word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in target_word_list:
    word = word.replace(i, ' ')
print(len(word))