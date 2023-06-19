num = 1
contador = maior = menor = media = soma = 0
continuar = ''
start = ''
finalizar = 'n'
while continuar != 'n' and start != 'n':
    start = str(input('Enter para continuar ou -n- para finalizar.'))
    if start == 'n':
        continuar=finalizar
    if start == '':
        while start != 'n':
            num = int(input('Digite um numero: '))
            contador += 1
            soma = soma+num
            if contador==1:
                maior=menor=num
            else:
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
                print('Digite -n- para finalizar')
                start=str(input('Enter para continuar?'))
