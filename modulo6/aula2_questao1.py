'''1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista.
Em seguida imprima na ordem estabelecida:
A lista ordenada, sem modificar a lista original
A lista original
O índice do maior valor da lista
O índice do menor valor da lista
'''
import random

lista = [random.randint(-100, 100) for i in range(20)]

print(lista)
print("------")
print(f"Lista ordenada: {sorted(lista)}")
print(f"Lista original: {lista}")
print(f"Índice de maior valor: {lista.index(max(lista))}")
print(f"Índice de menor valor: {lista.index(min(lista))}")