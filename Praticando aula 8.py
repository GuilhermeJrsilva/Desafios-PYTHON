#aqui eu importei o math e selcionei usando from e selecionando quais quero
from math import sqrt
num = int(input("Digite um número: "))
#a confusao veio aqui tendo que marca qual eu qeuro
raiz = sqrt(num)
#irei anotar no caderno algumas coisas sobre pois esta confuso agora um pouco
print ('A raiz de {} é igual a {:.2f}' .format(num, raiz))

#outro exemplo aqui sendo que aqui coloquei o ceil e deu resposta numero acima
#arredondou para inteiro e para cima
#aqui e so exemplo pois aqui nessa formula ja nao seria viavcel pela questao que aqui preciso
# dele querbrado mas so foi um exemplo
from math import ceil
n0= int(input('polegada'))
n1=int(input(' numerador'))
n2=int(input('denominador'))
s=(n0+(n1/n2))*25.4
print('e igua a {}'.format(ceil(s)))
#testando o tal do factorial
from math import factorial
n0= int(input('digite valor'))
s= factorial(n0)
print(f'{s}')