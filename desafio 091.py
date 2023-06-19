from random import randint
from time import sleep
from operator import itemgetter
jogadores=dict()
pessoas=list()
for j in range (0,4):
    jogador=str(input(f'Nome do {j+1}º Jogador: '))
    jogadores[jogador]=randint(1,6)
for k, v in jogadores.items():
    print(f'O Jogador {k} tirou {v} nos dados')
    sleep(1)
pessoas=sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'os jogadores foram {pessoas[0]}')
print('  ====   RANKING   ====  ')
for i, va in enumerate(pessoas):
    print(f'O {i+1}º foi {va[0]} que tirou {va[1]}')
    sleep(1)
