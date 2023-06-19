n=(int(input('Digite um valor para saber sua tabuada: ')))
for c in range (1,11):
    print('\033[31m{}\033[m X \033[32m{:2}\033[m = \033[33m{}\033[m'.format(n,c,(n*c)))