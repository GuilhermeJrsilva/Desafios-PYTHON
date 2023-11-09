nome=input ('Qual é seu nome?')
print(f'Prazer em te conhecer {nome:=^20}!')
n1= int(input ('Um valor:'))
n2= int(input ('Outro valor:'))
s=n1+n2
print('A soma vale {}'.format(s))
n1= int(input(' Um valor'))
n2= int(input(' outro valor'))
s= n1+n2
m=n1*n2
d=n1/ n2
di= n1//n2
e=n1**n2
#linha print foi colocado \n para quebra linha e usado tambem o end= para nao querbrar
# a linha mas o video ensina muita coisa video 7 minuto 23
print('soma e {}, \n o produto e {}, e a divisao e {}'.format(s,m,d), end=' ')
print('divisao inteira {}, e potencia {}'.format(di,e))

