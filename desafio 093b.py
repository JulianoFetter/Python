jogador={}
partidas=[]
jogador['nome']=str(input('Nome do Jogador: '))
tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantas gols na partida {c+1}? ')))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print('-*'*30)
print(jogador)
print('-*'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-*'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f'   => Na {i+1}ª partida fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols em {len(jogador["gols"])} jogos.')