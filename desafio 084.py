pessoas=[]
dado=[]
tot=0
mai=men=0

while True:
    print('\033[34m+=\033[m'*30)
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai=men=dado[1]
    else:
        if dado[1] > mai:
            mai=dado[1]
        if dado[1] < men:
            men=dado[1]
    pessoas.append(dado[:])
    dado.clear()
    tot+=1
    resp=str(input('Deseja continuar?[S/N] ')).strip().upper()
    if resp in 'Nn':
        break
print('\033[31m==\033[m'*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {mai}Kg, peso de ',end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()
print('--'*30)
print(f'O menor peso foi {men}Kg. peso de ',end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()
print('__'*30)