n1=float(input('Qual o valor do produto? R$'))
n2=float(input('Digite o desconto '))
v=n1-(n1*n2/100)
print(f'O novo valor do produto com desconto de {n2:.0f}% é de R${v:.2f}')
print('Top esse desconto!')
print('Muito obrigado!')
v2=n1-(n1*n2*2/100)
print(f'Se voce me der o dobro de desonto sera {v2}')
print('Que pena me mas valeu')
