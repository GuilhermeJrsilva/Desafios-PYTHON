a=float(input('Valor do cateto Oposto '))
b=float(input('Valor do cateto adjacente '))
a1= a**2
b1= b**2
c= a1+b1
c1= c**(1/2)
print('A hipotenusa e igual a',c1)

#aqui e usando as formas simples mas dando resultado do exercio
# e separei muito os calculo comparado com o do prof 
#mas abaixo farei conforme pedido que e importando modulos


from math import hypot
catop=float(input('valor cateto oposto '))
catadj=float(input('Valor cateto adjacente '))
print('A hipotenusa e igual a {}'.format(hypot(catop,catadj)))

#aqui usei tal modulo hypot deixou curto ficou top mas confuso
#outro tambem confuso e muita somas e linhas mas e top.


#aqui outro exemplo que prof fez 
co= float(input('Comprimento do cateto oposto'))
ca= float(input('Comprimento do cateto adjacente'))
hi= (co **2 + ca **2)**(1/2)
print('A hipotenusa vai medir {}'.format(hi))


#TODOS ACIMA COM RESULTADOS OTIMO MOSTRANDO QUE TEM VARIOS TIPO DE JEITO PARA ESCREVE LINHAS DE PROGRAMAS