import random
menbro1 = input('Digite o nome do 1° da Familia a ser sorteado: ')
menbro2 = input('Digite o nome do 2° da Familia a ser sorteado: ')
menbro3= input('Digite o nome do 3° da Familia a ser sorteado: ')
menbro4 = input('Digite o nome do 4° da Familia a ser sorteado: ')

lista_menbros =[menbro1, menbro2, menbro3, menbro4]

print(f'O nome sorteado é o(a);{random.choice(lista_menbros)} ')

#aqui tem foca no conehcimentos dos modulos

import random

# str e so para lembrar que tudo que ira ler e uma string poderia ja ir direto para o input
n1=str(input('Primeiro aluno '))
n2=str(input('Segundo aluno '))
n3=str(input('Terceiro aluno '))
n4=str(input('Quarto aluno '))

lista= [n1, n2, n3, n4]
# choice uma escolha dentro da lista
escolhido= random.choice(lista)

print('O aluno escolhida foi {}'. format(escolhido))

#o do prof mas aqui continua sendo modulos e esse nao teria jeiro se nao fosse  usando modulos