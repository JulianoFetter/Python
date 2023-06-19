print('Gerador de P.A.')
print('-*-'*20)
primeiro=int(input('Primeiro Termo: '))
razão=int(input('Razão: '))
termo=primeiro
cont=1
while cont <=10:
    print('{} -> '.format(termo), end='')
    termo+=razão
    cont=cont+1
print('FIM!')
