from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador= randint (0,2)
#print('O computador escolheu {}!'.format(itens[computador]))
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep (1)
print('PO!!!')
print('-='*12)
print('Compudador jogou {}!'.format(itens[computador]))
print('Jogador jogou {}!'.format(itens[jogador]))
print('-='*12)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador VENCE!')
    elif jogador == 2:
        print('Computador VENCE!')
    else:
        print('Jogada Invalida!')
elif computador == 1:
    if jogador == 0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCE!')
    else:
        print('Jogada Invalida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCE!')
    elif jogador == 1:
        print('Computador VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Invalida!')
