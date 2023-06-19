cadastro={}
lista=[]
mulheres=[]
contador=media=totidade=0
listaacima=[]
while True:
    print('-*' * 30)
    print(f' =-= CADASTRO DA {contador+1}º PESSOA! =-= ')
    while True:
        nome=str(input(f'Informe o Nome: '))
        if nome.isalpha() == True:
            cadastro['nome']=nome
            break
    idade=int(input('Informe a Idade: '))
    cadastro['idade']=idade
    totidade+=idade
    while True:
        sexo=str(input('Informe o Sexo [M/F]: ')).strip().upper()
        if sexo in 'MF':
            cadastro['sexo']=sexo
            if sexo in 'F':
                mulheres.append(nome)
            break
    contador+=1
    media = totidade / contador
    lista.append(cadastro.copy())
    while True:
        print('-*' * 30)
        continuar=input('Quer continuar?[S/N]: ').strip().upper()
        if continuar in 'SN':
                break
    if continuar in 'N':
        break
for p in lista:
    if p['idade'] >= media:
        for k ,v in p.items():
            listaacima.append(v)
print('-*'*30)
print(f'Foram cadastradas {contador} Pessoas.')
print(f'A media de idade do grupo é {media:.0f}')
print(f'As mulheres cadastradas foram {mulheres}.')
print(f'As pessoas com idade acima da media são {listaacima}')
