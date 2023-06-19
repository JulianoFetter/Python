from random import randint
#from time import sleep
computador = randint(0, 5)
#print('-=-* 20')
#print('vou pensar em um numero entre 0 e 5. tente adivinhas...')
#print('-=-* 20')
jogador = int(input('em que numero pensei?'))
#sleep(1)
if jogador == computador:
    print('PARABENS, você me venceu!')
else:
    print('GANHEI! Pensei no numero {} e você no numero {}'.format(computador, jogador))