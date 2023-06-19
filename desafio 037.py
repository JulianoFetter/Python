numero=int(input('Informe um numero inteiro:'))
print('''escolha uma opção para converção:
[1] para binário
[2] para octal
[3] para hexadecimal''')
base=int(input('Sua opção: '))
if base == 1:
    print ('{} convertido para BINARIO é igual a: {}'.format(numero,bin(numero)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(numero,oct(numero)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(numero,hex(numero)[2:]))
else:
    print('opção invalida!')