alunos = []
while True:
    print('*-'*20)
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    alunos.append([nome, [nota1, nota2], media])
    cont = (str(input('Quer continuar?[S/N] '))).strip().upper()
    if cont in 'N':
        print('==' * 20)
        break
print('---- BOLETIM! ----')
print('-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(alunos):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    resp = int(input('Mostras notas de qual aluno?(999)p/ Finalizar: '))
    if resp == 999:
        print('FINALIZANDO...')
        break
    resp-=1
    if resp <= len(alunos):
        print('-'*30)
        print(f'Notas de \033[33m{alunos[resp][0]}\033[m são \033[31m{alunos[resp][1]}\033[m')
print('<<< VOLTE SEMPRE >>>')
