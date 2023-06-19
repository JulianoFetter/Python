m=float(input('Insira a distância em metros:'))
km=m/1000
ht=m/100
dc=m/10
dm=m*10
cm=m*100
mm=m*1000
print('a medida de {} metros corresponde a \n{} kilometros \n{} hectometros \n{} decametros \n{:.0f} decimetros\n{:.0f} centimetros\n{:.0f} milimetros'.format(m,km,ht,dc,dm,cm,mm))
