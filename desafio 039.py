from datetime import date
ano=int(input('Digite o ano de seu nascimento:'))
idade=((date.today().year)-ano)
if idade < 18:
    print('Você tem {} anos e ainda faltam {} ano/s para se alistar!'.format(idade,(18-idade)))
    print('Seu alistamento será em {}!'.format(ano+18))
elif idade == 18:
    print('Você tem {} anos e deve se alistar este ano!'.format(idade))
elif idade > 18:
    print('Você tem {} anos e ja passou {} ano/s do periodo de se alistar!'.format(idade,(idade - 18)))
    print('Seu alistamento foi em {}!'.format(ano+18))
