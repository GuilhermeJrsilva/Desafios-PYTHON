n1=float(input('Nota do primeiro semestre '))
n2=float(input('Nota do segundo semestre '))
# na linha 4 precisamos somar antes de dividir entao nesse caso
#temos que colocar parenteses para forcar a somar primeiro e depois dividir
s=(n1+n2)/2
print(f'A media do ano do aluno foi {s}')