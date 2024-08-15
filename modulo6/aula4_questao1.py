'''1) Escreva um script python que use compreensão de listas para criar as seguintes listas:
Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
Todos os números entre 1 e 100 que sejam divisíveis por 7
Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento
(ex: ['par', 'impar',… , 'impar'])'''

pares = [i for i in range(20,50,2)]
print(f"Lista de números pares: {pares}")
print("----------")
lista_quadrado = [1,2,3,4,5,6,7,8,9]
quadrado = [n**2 for n in lista_quadrado]
print(f"Lista original: {lista_quadrado}")
print(f"Lista de quadrados: {quadrado}")
print("----------")
divisiveis7 = [i for i in range(1,100) if i % 7 == 0]
print(f"Lista de dívisíveis por 7: {divisiveis7}")
print("----------")
par_impar_original = [i for i in range(0,30,3)]
par_impar = ["par" if i % 2 == 0 else "impar" for i in range(0,30,3)]
print(f"Lista original: {par_impar_original}")
print(f"Lista paridade: {par_impar}")