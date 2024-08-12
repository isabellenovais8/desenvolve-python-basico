'''4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma
quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma
terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos
remanescentes da maior lista.

Exemplo de interação via terminal (entradas em negrito):
Digite a quantidade de elementos da lista 1: 4
Digite os 4 elementos da lista 1:
1 - 2 - 3 - 4
Digite a quantidade de elementos da lista 2: 6
Digite os 6 elementos da lista 2:
5 - 6 - 7 - 8 - 9 - 10
Lista intercalada: 1 5 2 6 3 7 4 8 9 10
'''

lista1 = [int(x) for x in input("Digite os números da primeira lista (separados por espaço): ").split()]
lista2 = [int(x) for x in input("Digite os números da segunda lista (separados por espaço): ").split()]
lista_intercalada = []

# Calcula o tamanho da menor lista
lista_menor = min(len(lista1), len(lista2))

# Intercale os elementos até o final da menor lista
for i in range(lista_menor):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adicione os elementos remanescentes da maior lista
lista_intercalada.extend(lista1[lista_menor:])
lista_intercalada.extend(lista2[lista_menor:])

print(f"Lista intercalada: {lista_intercalada}")