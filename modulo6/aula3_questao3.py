'''3) Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo
que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir
a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]'''

import random

lista = [random.randint(-10, 10) for i in range(20)]
print(f"Lista original: {lista}")

inicio_fatia_maior, tamanho_fatia_maior = 0, 0
inicio_fatia_atual, tamanho_fatia_atual = 0, 0

#Encontrar o intervalo que possui mais números
for i in range(len(lista)):
    if lista[i] < 0:
        tamanho_fatia_atual += 1
        if tamanho_fatia_atual == 1:
            inicio_fatia_atual = i
    else:
        if tamanho_fatia_atual > tamanho_fatia_maior:
            tamanho_fatia_maior = tamanho_fatia_atual
            inicio_fatia_maior = inicio_fatia_atual
        tamanho_fatia_atual = 0

print(inicio_fatia_maior, tamanho_fatia_maior)
del lista[inicio_fatia_maior:inicio_fatia_maior+tamanho_fatia_maior]
print(f"Lista editada: {lista}")