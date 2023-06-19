from random import randint
numeros=(randint(0,10),randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores foram:')
for n in numeros:
    print(f' {n}  ',end='')
print(f'\nO maior numero foi {max(numeros)}')
print(f'O menor numero foi {min(numeros)}')