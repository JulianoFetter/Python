numeros=[[],[]]
for c in range (0,7):
    num=(int(input(f'Digite o {c+1}º numero: ')))
    if num%2 ==0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os Numeros digitados foram: {numeros}.')
print()
print(f'Os valores Pares digitados foram:{numeros[0]}.')
print()
print(f'Os valores Impares digitdos foram: {numeros[1]}.')
