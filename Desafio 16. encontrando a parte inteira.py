# aqui usando importçao 
import math
n=float(input('Digite um valor '))
print(f'O número {n} tem a parte inteira {math.trunc(n)}')

#aqui usando oque ja se tem no proprio escrito exemplo o "int"
n= float(input('Digite um valor'))
print('O valor digitado foi {} e sua porçao inteira e {}' . format(n, int(n)))

#aqui so para lembra de como usar o format asim somente o "f"
print(f' O valor digitado foi {n} e sua porçao inteira e,  {int(n)}')
