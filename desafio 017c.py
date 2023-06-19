hi=float(input('diga o valor da hipotenusa '))
c1=float(input('diga o valor do cateto '))
hi2=hi**2
c12=c1**2
c22=(hi2-c12)
print('o cateto que esta faltando mede {}'.format(c22**(1/2)))