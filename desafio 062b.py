print('Gerador de P.A.')
print('-*-'*20)
primeiro=int(input('Primeiro Termo: '))
razão=int(input('Razão: '))
termo=primeiro
cont=1
total=0
mais=10
while mais !=0:
    total=total+mais
    while cont <=total:
        print('{} -> '.format(termo), end='')
        termo+=razão
        cont=cont+1
    print('PAUSA')
    mais=int(input('Quantos termos você quer ver a mais? '))
print('FIM!')
print('No total forma mostrados {} TERMOS.'.format(total))