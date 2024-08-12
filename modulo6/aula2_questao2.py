'''2) Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada
num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a
num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
A lista elementos
A soma dos valores da lista
A média dos valores da lista
'''

import random

num_elementos = random.randint(5, 20)
print(f"Número gerado: {num_elementos}")

lista = [random.randint(1, 10) for i in range(num_elementos)]

print(f"Valores da lista: {lista}")
print(f"Soma dos valores: {sum(lista)}")

media = sum(lista) / len(lista)
print(f"Média dos valores: {media:.2f}")