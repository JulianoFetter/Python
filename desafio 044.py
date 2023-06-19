valor=float(input('Informe o valor do produto R$ '))
condições=int(input('''Informe as condições de pagamento:'
-1- para à vista
-2- para 2x (somente no catão)
-3- para 3x ou mais (somente no cartão)'''))
if condições == 1:
    pagamento=int(input('''Informe a forma de pagamento:
    -1- para cheque
    -2- para cartão
    -3- para dinheiro '''))
    if pagamento == 3 or pagamento == 1:
        print('O produto terá um desconto de 10% e custará R${:.2f}!'.format(valor-(valor*(10/100))))
    elif pagamento == 2:
            print('O produto terá um desconto de 5% e custará R${:.2f}'.format(valor-(valor*(5/100))))
elif condições == 2:
    print('O produto não terá nem acrescimos, nem desconto e será parcelado em 2x de R${:.2f}'.format(valor/2))
elif condições == 3:
    parcelas = int(input('Em quantas vezes deseja parcelar? '))
    if parcelas >= 3:
        print('O produto terá um acrescimo de 20% passando a custar {:.2f} e será parcelado em {}x de R${:.2f}'.format(valor+(valor*20/100),parcelas,(((valor+(valor*20/100))/parcelas))))
else:
    print('\033[31mOpção Invalida!\033[m')
