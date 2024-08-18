'''Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os
seus índices da string. Dica: letra in "aeiou". Exemplo:'''

def cont_vogais(x):
    vogais = "aeiou"
    vogais_contador = 0
    indice = {}

    for index, char in enumerate(x.lower()):
        if char in vogais:
            vogais_contador += 1
            if char in indice:
                indice[char].append(index)
            else:
                indice[char] = [index]
    
    return vogais_contador, indice

frase = input("Digite a frase: ")

vogais_contador, indice_vogais = cont_vogais(frase)

print(f"Número de vogais: {vogais_contador}")
print(f"índices: {indice_vogais}")