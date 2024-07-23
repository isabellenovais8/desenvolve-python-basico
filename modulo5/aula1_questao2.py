'''Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores.
Peça ao usuário o valor de n

    Biblioteca random: Função randint()
    Biblioteca math: Função sqrt()'''

import random
import math

n = int(input("Informe o valor de n: "))
soma = 0

for i in range(n):
    x = random.randint(0,100)
    print(x)
    soma += x
    
print(f"A raíz quadrada da soma dos valores é: {math.isqrt(soma):.2f}")