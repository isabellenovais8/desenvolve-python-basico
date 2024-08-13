'''1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo
menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
A lista original
Os 3 primeiros elementos
Os 2 últimos elementos
A lista invertida (do fim para o começo)
Os elementos de índice par (0, 2, 4 … )
Os elementos de índice ímpar (1, 3, 5, … )'''

lista = [int(x) for x in input("Digite os números da lista: ").split()]

print(f"Lista original: {lista}")
print(f"3 primeiros elementos: {lista[0:3]}")
print(f"2 últimos elementos: {lista[-2:]}")
print(f"Lista invertida: {lista[::-1]}")
print(f"Elementos de índice par: {lista[::2]}")
print(f"Elementos de índice ímpar: {lista[1::2]}")