numeros=[]
pares=[]
impares=[]
c=pa=im=0
print('-='*30)
while True:
    numeros.append(int(input(f'Digite o {c+1}º Numero: ')))
    c+=1
    sn=' '
    while sn not in 'SN':
        sn=str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if sn == 'N':
            break
    if sn == 'N':
        break
for i ,v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
        pa+=1
    else:
        impares.append(v)
        im+=1
numeros.sort()
impares.sort()
pares.sort()
pa=len(pares)
im=(len(impares))
print('-' * 30)
print(f'Foram Digitados {c} Numeros.')
print(f'São eles: {numeros}')
print('-' * 30)
print(f'{pa} Foram PARES e {im} foram IMPARES.')
print(f'Os Numeros IMPARES são {impares}')
print(f'Os Numeros PARES são {pares}')
print('-='*30)