dict = {'a': 'hello', 'c': 'world', 'd': 'hello2', 'b': 'world2', 'x': 'hello3', 'g': 'world4'}
for key in sorted(dict):
    print(f'{key}: {dict[key]}')