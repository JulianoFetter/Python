from random import randint
from time import sleep
computador = randint(0, 10)
jogador=0
tentativas=0
print('-=-'* 20)
print('vou pensar em um numero entre \033[31m0\033[m e \033[31m10\033[m. tente adivinhas...')
sleep(1)
print('...')
sleep(1)
print('-=-'* 20)
while jogador != computador:
    jogador = int(input('em que numero pensei?'))
    if jogador == computador:
        print('PARABENS, você me venceu! Ambos pensamos no numero \033[31m{}\033[m !'.format(computador))
    else:
        print('ERROU!! Tente novamente!')
        tentativas+=1
print('Você precisou de \033[4;31m{}\033[m tentativas para me Vencer!'.format(tentativas+1))