from math import radians,sin,cos,tan
a=float(input('informe o angulo desejado:'))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('o angulo {}º tem \nSENO {:.2f}\nCOSSENO {:.2f} \nTANGENTE {:.2f}'.format(a,s,c,t))
