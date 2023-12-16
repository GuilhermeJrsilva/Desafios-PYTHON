n0=int(input('Polegada: Quando for somente polegada colocar 1 no denominador. Se for somente fraçao colocar 0= '))
n1=int(input('Numerador   = '))
n2=int(input('denominador = '))
s=(n0+(n1/n2))*25.4
print(f'{s:.2f}mm')