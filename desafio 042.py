r1=float(input('Primeiro segmento:'))
r2=float(input('Segundo segmento:'))
r3=float(input('Terceiro segmento:'))
if r1 < r2 +r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos {}, {} e {} PODEM formar um triangulo!'.format(r1,r2,r3))
    if r1 == r2 == r3:
        print('Forma um triangulo EQUILATERO!')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 !=r1 or r3 == r1 and r3!= r2:
        print('Forma um triangulo ISÓCELES!')
    elif r1 != r2 != r3 != r1:
        print('Forma um triangulo ESCALENO')
else:
    print('Os segmentos {}, {} e {} NÃO podem formar um triangulo!'.format(r1,r2,r3))
