str = input('Введите строку:')
str = str.lower()
dict ={}
for item in str:
    if item not in dict.keys():
        dict[item] = 1
    else:
        dict[item] += 1
print(dict)


