cores={'limpa':'\033[m',
       'ciano':'\033[34m',
       'roxo': '\033[35m',
       'amarelo':'\033[33m',
       'azul':'\033[34m',
       'vermelho':'\033[31m',
       'verde':'\033[32m'}
n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
m=(n1+n2)/2
print ('a media entre as notas {}{:.1f}{} e {}{:.1f}{} é \033[4m{}{:.1f}{}!'.format(cores['ciano'],n1,cores['limpa'],cores['roxo'],n2,cores['limpa'],cores['amarelo'],m,cores['limpa']))
if m < 5:
    print('{}REPROVADO!{}, estude mais'.format(cores['vermelho'],cores['limpa']))
elif m > 5 and m < 6.9:
    print('{}RECUPERAÇÃO!{}, não desista!'.format(cores['amarelo'],cores['limpa']))
elif m > 7:
    print('{} APROVADO!!!{} Meus parabens!'.format(cores['verde'],cores['limpa']))
