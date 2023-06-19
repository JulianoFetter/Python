n1 = float(input('Digite o 1º Valor: '))
n2 = float(input('Digite o 2º Valor: '))
r=0
while r != 5:
    print('-*-*'*15)

    print('Os Valores informados são \033[31m{}\033[m e \033[31m{}\033[m'.format(n1,n2))
    print('''Você quer:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do Programa''')
    r=int(input('Sua opção: '))
    if r==5:
        print('Fim do Programa!')
        print('Volte Sempre!')
    if r == 4:
        n1 = float(input('Digite o 1º Valor: '))
        n2 = float(input('Digite o 2º Valor: '))
    if r == 1:
        print('\033[31m{}\033[m + \033[31m{}\033[m = \033[33m{}\033[m'.format(n1,n2,(n1+n2)))
    if r == 2:
        print('\033[31m{}\033[m x \033[31m{}\033[m = \033[33m{:.2f}\033[m'.format(n1,n2,(n1*n2)))
    if r == 3:
        if n1 > n2:
            print('O MAIOR valor entre \033[31m{}\033[m e \033[31m{}\033[m é \033[33m{}\033[m'.format(n1,n2,n1))
        elif n2 > n1:
            print('O MAIOR valor entre \033[31m{}\033[m e \033[31m{}\033[m é \033[33m{}\033[m'.format(n2, n1, n2))
        elif n1 == n2:
            print('Ambos os valores tem o mesmo valor')
