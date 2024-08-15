'''2) Solicite uma frase do usuário e usando compreensão de listas imprima:
A lista de vogais da frase, ordenada alfabeticamente
A lista de consoantes da frase
Exemplo:
Digite uma frase: Eu gosto de programar em Python
Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']'''

frase = input("Digite uma frase: ")

vog = 'aeiou'

frase = frase.lower()
vogais = [letra for letra in frase if letra in vog]
consoantes = [letra for letra in frase if letra.isalpha() and letra not in vog]

vogais_alf = sorted(vogais)

print(f"Vogais: {vogais_alf}")
print(f"Consoantes: {consoantes}")
