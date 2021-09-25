a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))
d = int(input('Введите четвертое число:'))

print(' ', end=' ')
for el in range(c, d+1):
    print(str(el).rjust(4), end=' ')
print()
for el in range(a, b+1):
    print(el, end=' ')
    for el2 in range(c, d+1):
        print(str(el*el2).rjust(4), end=' ')
    print()