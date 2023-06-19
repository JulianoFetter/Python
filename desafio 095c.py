lista=list()
jogador={}
partidas=[]
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome do Jogador: '))
    tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantas gols na partida {c+1}? ')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    partidas.clear()
    lista.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Comando inválido!')
    print('-*'*30)
    if resp == 'N':
        break
for i , va in enumerate(lista):
    print(f'{i:<4}', end='')
    for v in va.values():
        print(f'{str(v):<10}',end='')
    print()
print('-*' * 30)
while True:
    aprov=int(input('Qual o jogador que quer ver o aproveitamento (999 p/ encerrar): '))
    if aprov == 999:
        print('-*' * 30)
        break
    if aprov > len(lista):
        print('Comando invalido!')
        print('-*' * 30)
    for u, p in enumerate(lista[aprov]['gols']):
        print(f'Na {u+1}ª Partida, {lista[aprov]["nome"]} fez {p} gols',end='')
        print()
    print(f'{lista[aprov]["nome"]} fez um total de {lista[aprov]["total"]} gols em {len(lista[aprov]["gols"])} jogos, com uma media de {(lista[aprov]["total"]/len(lista[aprov]["gols"])):.1f} por partida.')
    print('-*' * 30)