print('Sequencia de Fibonacci')
print('-'*20)
n=int(input('Digite um valor para mostrar sua Sequencia Fibonacci: '))
n1=n
cont=int(input('Informe o numero de termos: '))
c=0
n2=0
n3=0
total=0
mais=cont-1
print('{}-'.format(n1),end='')
while mais != 0:
    total=total+mais
    while c != total:
        n3=n1+n2
        n2=n1
        n1=n3
        c=c+1
        print('-{}-'.format(n3),end='')
    print('PAUSA')
    mais=int(input('Quantas termos a mais quer ver? '))
    print('-'*20)
print('FIM!')
print('No total forma mostrados {} TERMOS.'.format(total+1))