a = input('Введите число: ')
a = int(a)
list = []
for item in range(1, a+1):
    if a % item == 0:
        list.append(item)
print(list)






