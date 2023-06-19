print('Gerador de P.A.')
print('-*-'*20)
e=1
while e != 0:
    primeiro=int(input('Primeiro Termo: '))
    razão=int(input('Razão: '))
    termo=primeiro
    contador=int(input('Quantos termos quer vizualizar? (digite 0 para encerrar)'))
    cont=1
    if contador == 0:
        e = contador
    while cont <= contador:
        print('{} -> '.format(termo), end='')
        termo+=razão
        cont=cont+1
    print('FIM!')

