peso=float(input('Informe o seu peso:'))
altura=float(input('Infome sua altura em metros:'))
imc=(peso/(altura**2))
imcideal1=(18.5*(altura**2))
imcideal2=(24.9*(altura**2))
print('Seu IMC é: \033[31m{:.2f}\033[m'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso')
    print('você deve engordar entre Kg {:.2f} e Kg {:.2f}!'.format((imcideal1-peso),(imcideal2-peso)))
elif imc >= 18.5 and imc < 25:
    print('Seu peso está ideal!')
elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso!')
    print('Você deve emagrecer entre Kg {:.2f} e Kg {:.2f}!'.format((peso-imcideal1),(peso-imcideal2)))
elif imc >= 30 and imc < 40:
    print('Você está obeso!')
    print('Você deve emagrecer entre Kg {:.2f} e Kg {:.2f}!'.format((peso - imcideal1), (peso - imcideal2)))
elif imc >= 40:
    print('Você esta com obesidade Morbida!')
    print('Você deve emagrecer entre Kg {:.2f} e Kg {:.2f}!'.format((peso - imcideal1), (peso - imcideal2)))
