num = 1
contador = 0
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999
media = 0
soma = 0
continuar = ('')

while continuar != 'n':
    num = int(input('Digite um numero: '))
    contador += 1
    soma = soma+num
    print('Digite -s- para continuar é -n- para finalizar')
    continuar = str(input('Deseja continuar?'))
    if maior < num:
        maior=num
    if menor > num and num > 0:
        menor=num
    if continuar == 'n':
        print('''foram digitados um total de {} numeros
                    a soma total é {}
                    a média é {:.2f}
                    o maior valor é {}
                    o menor valor é {}'''.format((contador), soma, (soma / (contador)), maior, menor))


