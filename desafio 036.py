salario=float(input('Informe seu salário mensal: R$'))
valorc=float(input('Informe o valor da casa que deseja comprar: R$'))
anos=float(input('Informe em quantos anos pretende quitar a divida:'))
prestacao=valorc/(anos*12)
trinta=salario*(30/100)
if prestacao <= trinta:
    print('APROVADO! Comprando uma casa no valor de R${:.2f} suas parcelas ficam de R${:.2f} mensais'.format(valorc,prestacao))
else:
    print('NEGADO! Comprando uma casa no valor de R${:.2f} suas parcelas ultrapassam os 30% do seu salario'.format(valorc))
    print('O valor maximo das parcelas para o seu salario é de R${:.2f} e nessas condiçoes ficam de R${:.2f}'.format(trinta,prestacao))
    print('estando assim R${:.2f} acima do valor maximo!'.format(prestacao-trinta))