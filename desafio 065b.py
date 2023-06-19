num = 1
contador = 0
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999
media = 0
soma = 0
continuar = ''
start = ''
finalizar = 'n'
r=0
while continuar == '' and finalizar == 'n':
    print('escolha uma opção:')
    print('''[1] digitar novos valores
[2] continuar digitando
[3] encerrar o programa''')
    print('-' * 15)
    r=int(input('Sua opção: '))
    if r == 3:
        continuar=finalizar
    elif r==1 or r==2:
        if r==1:
            start = ''
            num = 1
            contador = 0
            maior = 0
            menor = 9999999999999999999999999999999999999999999999999999999
            media = 0
            soma = 0
        elif r ==2:
            start = ''
        if start == '':
            while start != 'n':
                num = int(input('Digite um numero: '))
                contador += 1
                soma = soma+num
                if maior < num:
                    maior=num
                if menor > num and num > 0:
                    menor=num
                start = str(input('Enter para continuar ou -n- para finalizar.'))
                if start == 'n':
                    print('''foram digitados um total de {} numeros
            a soma total é {}
            a média é {:.2f}
            o maior valor é {}
            o menor valor é {}'''.format((contador), soma, (soma / (contador)), maior, menor))
                    print('Digite -n- para voltar ao menu.')
                    start=str(input('Enter para continuar.'))
                    if start == 'n':
                        continuar=''