valor=float(input('qual o valor real do produto? R$'))
avista=valor-(valor*12/100)
prazo=valor+(valor*8/100)
desc=(valor-avista)
acres=(prazo-valor)
print('o produto que custa R${:.2f}\na vista passa a custar R${:.2f} com um desconto de R${:.2f} \ne a prazo sera R${:.2f} com um acrescimo de R${:.2f} '.format(valor,avista,desc,prazo,acres))