import random
f1=str(input('Qual nome do primeiro da Familia?'))
f2=str(input('Qual nome do segundo da Familia?'))
f3=str(input('Qual o nome do terceiro da Familia?'))

familia=((f1), (f2), (f3))

print(random.sample(familia,3))

# encontrei nos comentarios tentei fazer com base

import random
# str so para lembrar que ele esta lendo qualquer coisa numero escrita qualquer string
n1= str(input('Primeiro aluno'))
n2= str(input('Segundo aluno'))
n3=str(input('Terceiro aluno'))
n4=str(input('Qaurto aluno'))
lista= [n1, n2, n3, n4]

#shuffle embaralhar 
random.shuffle(lista)

print('A ordem de apresentaçao sera')
print(lista)

