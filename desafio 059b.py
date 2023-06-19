n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
opção=0
while opção!= 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opção=int(input('Qual é a sua opção?'))
    if opção == 1:
        soma= n1+n2
        print('A soma entre {} e {} é {}'.format(n1,n2,(n1+n2)))
    elif opção ==2:
        produto=n1*n2
        print('O resultado de {} x {} é {}'.format(n1,n2,(n1*n2)))
    elif opção == 3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('Entre {} e {} o MAIOR é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('informe os numeros novamente:')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif opção ==5:
        print('Finalizando...')
    else:
        print('Opção Invalida!')
    print('-=-'*10)
print('Volte Sempre!')