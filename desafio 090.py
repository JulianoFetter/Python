aluno=dict()
lista=list()
resp=' '
while resp not in 'N':
    aluno['nome']=str(input('Nome do aluno: '))
    aluno['media']=float(input('Média do aluno: '))
    if aluno['media'] >= 7:
        aluno['situação']='Aprovado'
    else:
        aluno['situação']='Reprovado'
    lista.append(aluno.copy())
    while True:
        print('-' * 20)
        resp=str(input('Quer continuar?[S/N] ')).strip().upper()
        if resp not in 'SN':
            print('-' * 20)
            print('Comando invalido')
        if resp in 'S':
            print('-'*20)
            print('PROX. ALUNO!')
            print('-*' * 20)
            break
        if resp in 'N':
            print('-' * 20)
            break
for e in lista:
    for k,v in e.items():
        print(f'{k} é igual a {v}')
    print('-' * 20)